#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets


def arayuz():
    object = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()


    window.setWindowTitle("Arayüz") # Arayüzü isimlendirme.
    window.setGeometry(300,300,600,480) # Arayüzün konumu ve çözünürlüğünü belirleme.

    radio1 = QtWidgets.QRadioButton(window) # Butonu tanımla.
    radio2 = QtWidgets.QRadioButton(window)
    radio3 = QtWidgets.QRadioButton(window)
    
    radio1.setText("Seçenek 1") # Butonu isimlendir
    radio2.setText("Seçenek 2")
    radio3.setText("Seçenek 3")
    
    radio1.move(100,50) # Butonu taşı
    radio2.move(100,70)
    radio3.move(100,90)
    
    radio3.setCheckable(False) # Butona tıklamayı engelle.

    window.show() # Arayüzü göster.
    sys.exit(object.exec_())


arayuz()
