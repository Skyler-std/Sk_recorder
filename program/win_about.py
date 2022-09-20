# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_about.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
import cv2, sys


class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("AboutWindow")
        AboutWindow.resize(412, 372)
        AboutWindow.setMinimumSize(QtCore.QSize(412, 372))
        AboutWindow.setMaximumSize(QtCore.QSize(412, 372))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        AboutWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/all.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutWindow.setWindowIcon(icon)
        self.AboutLabel = QtWidgets.QLabel(AboutWindow)
        self.AboutLabel.setGeometry(QtCore.QRect(50, 120, 301, 121))
        self.AboutLabel.setObjectName("AboutLabel")
        self.AboutDealLabel = QtWidgets.QLabel(AboutWindow)
        self.AboutDealLabel.setGeometry(QtCore.QRect(10, 310, 391, 51))
        self.AboutDealLabel.setObjectName("AboutDealLabel")
        self.AboutLinkLabel = QtWidgets.QLabel(AboutWindow)
        self.AboutLinkLabel.setGeometry(QtCore.QRect(50, 240, 301, 61))
        self.AboutLinkLabel.setObjectName("AboutLinkLabel")
        self.graphicsView = QtWidgets.QGraphicsView(AboutWindow)
        self.graphicsView.setGeometry(QtCore.QRect(152, 10, 100, 100))
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView.setForegroundBrush(brush)
        self.graphicsView.setInteractive(False)
        self.graphicsView.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.graphicsView.setObjectName("graphicsView")

        # 显示logo及解决透明问题
        self.scene = QtWidgets.QGraphicsScene()
        img = cv2.imread("..//img//about.png")
        cvimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        y, x = img.shape[:-1]
        frame = QImage(cvimg, x, y, QImage.Format_RGB888)
        self.pix = QPixmap.fromImage(frame)
        self.scene.addPixmap(self.pix)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "关于"))
        self.AboutLabel.setText(_translate("AboutWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Sk_recorder</span></p><p>软件作者: Skyler Sun</p><p>软件遵循GPLv3.0协议, 详情请访问软件地址</p><p>软件版本v0.1.0</p></body></html>"))
        self.AboutDealLabel.setText(_translate("AboutWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:9pt; font-weight:600; color:#ff0000;\">声明: 本软件仅供学习交流和日常使用, 如作他用所承担的法律责任一概与</span></p><p align=\"justify\"><span style=\" font-size:9pt; font-weight:600; color:#ff0000;\">作者无关(下载使用即代表你同意上述观点)</span></p></body></html>"))
        self.AboutLinkLabel.setText(_translate("AboutWindow", "<html><head/><body><p><a href=\"3385213313@qq.com\"><span style=\" text-decoration: underline; color:#0000ff;\">3385213313@qq.com</span></a></p><p><a href=\"https://github.com/Skyler-std/Sk_recorder\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/Skyler-std/Sk_recorder</span></a></p></body></html>"))


AboutWindow = QtWidgets.QMainWindow()
ui_about = Ui_AboutWindow()
ui_about.setupUi(AboutWindow)
