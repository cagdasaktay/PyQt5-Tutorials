#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets


def arayuz():
    object = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()


    window.setWindowTitle("Arayüz") # Arayüzü isimlendirme.
    window.setGeometry(300,300,600,480) # Arayüzün konumu ve çözünürlüğünü belirleme.

    spin = QtWidgets.QDoubleSpinBox(window) # Spin Box'ı ekleme (Float spin box eklenir)
    spin.setRange(5,25) # başlangıç ve bitiş değerleri
    spin.setSingleStep(1.25) # Değişimi belirle (1.25 er artar)
    

    window.show() # Arayüzü göster.
    sys.exit(object.exec_())


arayuz()
