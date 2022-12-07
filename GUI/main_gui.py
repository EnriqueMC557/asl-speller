# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 17:12:55 2022

@author: sleyv
"""

import sys
sys.path.append('../yolov5')

import cv2
import torch
from statistics import mode
from asl_speller import Ui_ASLSPELLER
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap

from models.common import DetectMultiBackend
from utils.dataloaders import LoadStreams
from utils.torch_utils import select_device
from utils.general import check_img_size, Profile, non_max_suppression, check_imshow, scale_boxes
from utils.plots import Annotator, colors


weights = '../yolov5/runs/train/exp/weights/best.pt'


class Asl_gui(QWidget):
    def __init__(self, parent=None):
        """Inicializador de GUI."""
        QWidget.__init__(self, parent)
        self.ui = Ui_ASLSPELLER()
        self.ui.setupUi(self)
        self.timer_result = QTimer()
        self.results = []
        self.space = '  '
        self.palabra = ''
        self.dataset = None
        self.bs = None
        self.view_img = None
        self.vid_stride = 1
        self.device = select_device('')
        self.model = DetectMultiBackend(weights, device=self.device, dnn=False, data='data/coco128.yaml', fp16=False)
        self.stride, self.names, self.pt = self.model.stride, self.model.names, self.model.pt
        self.imgsz = check_img_size((640, 640), s=self.stride)  # check image size

        self.ui.startbutton.clicked.connect(self.iniciar)
        self.ui.finishbutton.clicked.connect(self.finish)
        self.ui.finishbutton.setDisabled(True)
        self.timer_result.timeout.connect(self.updateTextResult)

    def updateTextResult(self):
        if len(self.results) > 0:
            mode_class = mode(self.results)
            letra = self.space if str(self.names[mode_class]) == 'nothing' else str(self.names[mode_class])
            self.palabra += letra
            self.ui.text_result.setText(self.palabra)
            self.results = []

    def iniciar(self):
        self.timer_result.start(2000)
        self.ui.text_result.setText('')

        self.ui.startbutton.setDisabled(True)
        self.ui.finishbutton.setDisabled(False)

        # SetUp inference
        self.view_img = check_imshow(warn=True)
        self.dataset = LoadStreams('0', img_size=self.imgsz, stride=self.stride, auto=self.pt, vid_stride=self.vid_stride)
        self.bs = len(self.dataset)

        self.model.warmup(imgsz=(1 if self.pt or self.model.triton else self.bs, 3, *self.imgsz))  # warmup
        seen, windows, dt = 0, [], (Profile(), Profile(), Profile())

        self.results = []
        try:
            for path, im, im0s, vid_cap, s in self.dataset:
                with dt[0]:
                    im = torch.from_numpy(im).to(self.model.device)
                    im = im.half() if self.model.fp16 else im.float()  # uint8 to fp16/32
                    im /= 255  # 0 - 255 to 0.0 - 1.0
                    if len(im.shape) == 3:
                        im = im[None]  # expand for batch dim

                # Inference
                with dt[1]:
                    pred = self.model(im, augment=False, visualize=False)

                # NMS
                with dt[2]:
                    pred = non_max_suppression(pred, 0.5, 0.45, None, False, max_det=1000)

                # Process predictions
                for i, det in enumerate(pred):  # per image
                    seen += 1
                    p, im0, frame = path[i], im0s[i].copy(), self.dataset.count
                    annotator = Annotator(im0, line_width=3, example=str(self.names))

                    if len(det):
                        # Rescale boxes from img_size to im0 size
                        det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], im0.shape).round()

                        # Print results
                        for c in det[:, 5].unique():
                            detected_class = int(c)
                            self.results.append(detected_class)

                        # Write results
                        for *xyxy, conf, cls in reversed(det):
                            # Add bbox to image
                            c = int(cls)  # integer class
                            label = f'{self.names[c]} {conf:.2f}'
                            annotator.box_label(xyxy, label, color=colors(c, True))

                    # Stream results
                    im0 = annotator.result()
                    rgbImage = cv2.cvtColor(im0, cv2.COLOR_BGR2RGB)
                    h, w, ch = rgbImage.shape
                    bytesPerLine = ch * w
                    convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                    p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                    self.ui.camera_label.setPixmap(QPixmap.fromImage(p))
        except AttributeError:
            # Esto está bien, ocurre cuando se cierra la cámara
            pass

    def finish(self):
        self.dataset.cap.release()
        self.dataset = None
        self.ui.camera_label.setPixmap(QPixmap("webcam.jpg"))
        self.timer_result.stop()
        self.palabra = ''

        self.ui.startbutton.setDisabled(False)
        self.ui.finishbutton.setDisabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Asl_gui()
    gui.show()
    sys.exit(app.exec_())
