#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets


def arayuz():
    object = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()


    window.setWindowTitle("Arayüz") # Arayüzü isimlendirme.
    window.setGeometry(300,300,600,480) # Arayüzün konumu ve çözünürlüğünü belirleme.


    kontrol1 = QtWidgets.QCheckBox(window) # Butonu ekle.
    kontrol2 = QtWidgets.QCheckBox(window)
    kontrol3 = QtWidgets.QCheckBox(window)
     
    kontrol1.setText("Seçenek 1") # Butonu isimlendir
    kontrol2.setText("Seçenek 2")
    kontrol3.setText("Seçenek 3")
    
    kontrol1.move(100,50) # Butonu taşı
    kontrol2.move(100,70)
    kontrol3.move(100,90)
    
    kontrol3.setCheckable(False) # Butona tıklamayı engelle.


    window.show() # Arayüzü göster.
    sys.exit(object.exec_())


arayuz()
