# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 17:12:55 2022

@author: sleyv
"""

import sys
import cv2
from asl_speller import Ui_ASLSPELLER
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot, QTimer
from PyQt5.QtGui import QImage, QPixmap

# class Thread(QThread):
#     changePixmap = pyqtSignal(QImage)

#     def run(self):

#         while True:
#             ret, frame = self.cap.read()
#             if ret:
               
#                 rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                 h, w, ch = rgbImage.shape
#                 bytesPerLine = ch * w
#                 convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
#                 p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
#                 self.changePixmap.emit(p)
            

    
class Asl_gui(QWidget):
    def __init__(self,parent=None):
        """Inicializador de GUI."""
        QWidget.__init__(self,parent)
        self.ui = Ui_ASLSPELLER()
        self.ui.setupUi(self)
        self.cap = cv2.VideoCapture(0)
        self.timer_video = QTimer()
        self.timer_video.timeout.connect(self.setImage)
        self.ui.startbutton.clicked.connect(self.iniciar)
        self.ui.finishbutton.clicked.connect(self.finish)
        self.ui.finishbutton.setDisabled(True)
        
        
    def setImage(self):

        flag, frame = self.cap.read()
        if flag:
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgbImage.shape
            bytesPerLine = ch * w
            convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
            p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
            self.ui.camera_label.setPixmap(QPixmap.fromImage(p))
            
            
        
    def iniciar(self):
        self.ui.text_result.setText('Hola')
        
        if not self.timer_video.isActive():
         
            flag = self.cap.open(0)
            if flag == False:
                QMessageBox.warning(
                    self, "Warning", "No se pudo abrir", buttons=QMessageBox.Ok, defaultButton=QMessageBox.Ok)
            else:
                self.timer_video.start(30)
                self.ui.startbutton.setDisabled(True)
                self.ui.finishbutton.setDisabled(False)
        
    def finish(self):
        self.ui.text_result.setText('bye')

        self.ui.camera_label.setPixmap(QPixmap("webcam.jpg"))
        self.timer_video.stop()
        self.cap.release()

        self.ui.startbutton.setDisabled(False)
        self.ui.finishbutton.setDisabled(True)

        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Asl_gui()
    gui.show()
    
    
    sys.exit(app.exec_())
        
        
    