#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets


def arayuz():
    object = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()


    window.setWindowTitle("Arayüz") # Arayüzü isimlendirme.
    window.setGeometry(300,300,600,480) # Arayüzün konumu ve çözünürlüğünü belirleme.
    
    satir = QtWidgets.QLineEdit(window)
    satir.setReadOnly(True)
    buton = QtWidgets.QPushButton(window)

    buton.move(0,20)
    buton.setText("Gonder")
    
    def guncelle():
        satir.setText("1.22")
    
    buton.clicked.connect(guncelle) # Butona tıklandığında guncelle fonksiyonuna gider.
    


    window.show() # Arayüzü göster.
    sys.exit(object.exec_())


arayuz()
