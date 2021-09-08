#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets


def arayuz():
    object = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()


    window.setWindowTitle("Arayüz") # Arayüzü isimlendirme.
    window.setGeometry(300,300,600,480) # Arayüzün konumu ve çözünürlüğünü belirleme.

    label = QtWidgets.QLabel(window)
    label.setText("Sensör Paneli:") # Etiketi isimlendirme.
    label.move(100,200) # Etiketin konumunu belirleme.

    window.show() # Arayüzü göster.
    sys.exit(object.exec_())


arayuz()
