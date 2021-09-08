#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets,QtCore


def arayuz():
    object = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()


    window.setWindowTitle("Arayüz") # Arayüzü isimlendirme.
    window.setGeometry(300,300,600,480) # Arayüzün konumu ve çözünürlüğünü belirleme.

    slider = QtWidgets.QSlider(QtCore.Qt.Horizontal,window) # Slider Horizontal olarak eklenir
    slider.move(300,150) # Konumu belirlenir
    slider.setMinimum(0) # Slider'ın başlangıç değeri belirlenir
    slider.setMaximum(10) # Slider'ın bitiş değeri belirlenir
    slider.setTickPosition(QtWidgets.QSlider.TicksBelow) # Slider'ın altına tick eklenir.
    slider.setTickInterval(2) # Tick'lerin aralığı belirlenir. (2 değerde bir gözlemlenir.)
    slider.setValue(8) # Slider'ın default değeri 8 yapılır.

    window.show() # Arayüzü göster.
    sys.exit(object.exec_())


arayuz()
