#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets


def arayuz():
    object = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()


    window.setWindowTitle("Arayüz") # Arayüzü isimlendirme.
    window.setGeometry(300,300,600,480) # Arayüzün konumu ve çözünürlüğünü belirleme.

    buton1 = QtWidgets.QPushButton(window)
    buton2 = QtWidgets.QPushButton(window)
    buton3 = QtWidgets.QPushButton(window)
    buton4 = QtWidgets.QPushButton(window)
    buton1.setText("Buton 1")
    buton2.setText("Buton 2")
    buton3.setText("Buton 3")
    buton4.setText("Buton 4")
    
    yatay = QtWidgets.QHBoxLayout() # Yatay olarak tanımla
    dikey = QtWidgets.QVBoxLayout() # Dikey olarak tanımla
    dikey.addWidget(buton1) # Dikey olana buton1 ve buton2 yi ekle
    dikey.addWidget(buton2)
    yatay.addWidget(buton3) # Yatay olana buton1 ve buton2 yi ekle
    yatay.addWidget(buton4)
    
    dikey.addLayout(yatay) # Dikey ile yatayı birbirine ekle.
    
    window.setLayout(dikey) # Pencerede göster.


    window.show() # Arayüzü göster.
    sys.exit(object.exec_())


arayuz()
