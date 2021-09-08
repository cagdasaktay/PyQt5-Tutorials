#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets


def arayuz():
    object = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()


    window.setWindowTitle("Arayüz") # Arayüzü isimlendirme.
    window.setGeometry(300,300,600,480) # Arayüzün konumu ve çözünürlüğünü belirleme.

    line = QtWidgets.QLineEdit(window) # Satırı belirleme.

    line.setEchoMode(QtWidgets.QLineEdit.Password) # Satırdaki değeri gizleme. (password)
    #line.setText("2.4") # Satırdaki değeri belirleme.
    #line.setReadOnly(True) # Satırdaki değeri read-only yapma.


    window.show() # Arayüzü göster.
    sys.exit(object.exec_())


arayuz()
