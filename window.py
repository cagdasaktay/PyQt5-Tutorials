#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets


def arayuz():
    object = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()


    window.setWindowTitle("Arayüz") # Arayüzü isimlendirme.
    window.setGeometry(300,300,600,480) # Arayüzün konumu ve çözünürlüğünü belirleme.

    window.show() # Arayüzü göster.
    sys.exit(object.exec_())


arayuz()
