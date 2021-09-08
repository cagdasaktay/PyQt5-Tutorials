#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets


def arayuz():
    object = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()


    window.setWindowTitle("Arayüz") # Arayüzü isimlendirme.
    window.setGeometry(300,300,600,480) # Arayüzün konumu ve çözünürlüğünü belirleme.

    combo = QtWidgets.QComboBox(window) # Butonu ekle
    combo.addItem("scan") # Butonlara etiket ekle.
    combo.addItem("odom")
    combo.addItem("cmd_vel")
    
    print(combo.count()) # Combo box'ın içinde kaç tane buton olduğunu bastırır.
    
   # combo.setItemText(2,"kamera") # 2. indisi değiştirir. (cmd_vel yerine kamera gelir.)

    window.show() # Arayüzü göster.
    sys.exit(object.exec_())


arayuz()
