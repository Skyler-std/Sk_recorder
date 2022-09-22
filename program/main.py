# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Skyler
# date: 2022-9-15 19:27
from PyQt5 import QtWidgets
from win_main import Ui_MainWindow
from log import add_log
from qt_material import apply_stylesheet

from time import sleep
import os
import sys


def ck_path(path):
    # slip目录是否存在
    if not os.path.exists(path):
        os.mkdir(path)
    # slip目录是否为文件
    if os.path.isfile(path):
        os.remove(path)
        os.mkdir(path)


# 主程序开始
if __name__ == "__main__":
    add_log("#######Program started#######")
    sleep(0.1)
    add_log("Executing init...")
    ck_path('C:/slip')
    ck_path('C:/sshot')
    ck_path('C:/rrecord')
    with open('program_position.txt', 'w') as f:
        f.write(os.path.abspath(sys.argv[0]))
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_main = Ui_MainWindow()
    ui_main.setupUi(MainWindow)
    apply_stylesheet(app, theme='dark_cyan.xml')
    add_log("Init done")
    sleep(0.1)
    add_log("Start to show MainWindow")
    MainWindow.show()
    sys.exit(app.exec_())
