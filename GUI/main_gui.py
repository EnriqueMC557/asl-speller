# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 17:12:55 2022

@author: sleyv
"""

import sys
import cv2
from asl_speller import Ui_ASLSPELLER
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap

class Thread(QThread):
    changePixmap = pyqtSignal(QImage)

    def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
               
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
                
class Asl_gui(QWidget):
    def __init__(self,parent=None):
        """Inicializador de GUI."""
        QWidget.__init__(self,parent)
        self.ui = Ui_ASLSPELLER()
        self.ui.setupUi(self)
        self.ui.startbutton.clicked.connect(self.iniciar)
        self.ui.finishbutton.clicked.connect(self.finish)
        self.th = Thread(self)
        self.th.changePixmap.connect(self.setImage)
        
        
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.ui.camera_label.setPixmap(QPixmap.fromImage(image))   
        
    def iniciar(self):
        self.ui.text_result.setText('Hola')
        self.th.start()
        
        
        
        
    def finish(self):
        self.ui.text_result.setText('bye')
        self.th.terminate()
        self.ui.camera_label.setPixmap(QPixmap("webcam.jpg"))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Asl_gui()
    gui.show()
    
    
    sys.exit(app.exec_())
        
        
    