# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_donate.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DonateWindow(object):
    def setupUi(self, DonateWindow):
        DonateWindow.setObjectName("DonateWindow")
        DonateWindow.resize(261, 356)
        DonateWindow.setMinimumSize(QtCore.QSize(261, 356))
        DonateWindow.setMaximumSize(QtCore.QSize(261, 356))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        DonateWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/all.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DonateWindow.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(DonateWindow)
        self.label.setGeometry(QtCore.QRect(3, 1, 251, 351))
        self.label.setObjectName("label")

        self.retranslateUi(DonateWindow)
        QtCore.QMetaObject.connectSlotsByName(DonateWindow)

    def retranslateUi(self, DonateWindow):
        _translate = QtCore.QCoreApplication.translate
        DonateWindow.setWindowTitle(_translate("DonateWindow", "捐赠"))
        self.label.setText(_translate("DonateWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">感谢您的好意, 如果您喜欢</span></p><p><span style=\" font-size:16pt;\">本软件, 就将它分享给对的</span></p><p><span style=\" font-size:16pt;\">人吧, 谢谢!</span></p></body></html>"))


DonateWindow = QtWidgets.QWidget()
ui_donate = Ui_DonateWindow()
ui_donate.setupUi(DonateWindow)
