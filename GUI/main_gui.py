# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 17:12:55 2022

@author: sleyv
"""

import sys
from asl_speller import Ui_ASLSPELLER
from PyQt5.QtWidgets import QApplication, QWidget


class asl_gui(QWidget):
    def __init__(self,parent=None):
        """Inicializador de GUI."""
        QWidget.__init__(self,parent)
        self.ui = Ui_ASLSPELLER()
        self.ui.setupUi(self)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = asl_gui()
    gui.show()
    sys.exit(app.exec_())
        
        
    