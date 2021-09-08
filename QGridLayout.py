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
    
    mizanpaj = QtWidgets.QGridLayout() # Grid'i tanımla
    
    mizanpaj.addWidget(buton1,1,1) # Butonları ve konumlarını belirle
    mizanpaj.addWidget(buton2,1,2)
    mizanpaj.addWidget(buton3,2,1)
    mizanpaj.addWidget(buton4,2,2)
        
    window.setLayout(mizanpaj)

    window.show() # Arayüzü göster.
    sys.exit(object.exec_())


arayuz()
