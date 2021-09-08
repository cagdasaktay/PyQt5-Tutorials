#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets


def arayuz():
    object = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()


    window.setWindowTitle("Arayüz") # Arayüzü isimlendirme.
    window.setGeometry(300,300,600,480) # Arayüzün konumu ve çözünürlüğünü belirleme.

    etiket1 = QtWidgets.QLabel(window) # Label tanımlanır
    etiket2 = QtWidgets.QLabel(window)
    etiket1.setText("Konum x: ")
    etiket2.setText("Konum y: ")    
    
    satir1 = QtWidgets.QLineEdit(window) # Line tanımlanır
    satir2 = QtWidgets.QLineEdit(window)
    
    mizanpaj = QtWidgets.QFormLayout() # Form tanımla
    mizanpaj.addRow(etiket1,satir1) # Satirlar eklenir
    mizanpaj.addRow(satir2,etiket2) # argümanların konumları değiştirilebilir.
    
    window.setLayout(mizanpaj)


    window.show() # Arayüzü göster.
    sys.exit(object.exec_())


arayuz()
