# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\peng\PythonProjects\Sk_recorder\ui\win_record_load.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RecordLoad(object):
    def setupUi(self, RecordLoad):
        RecordLoad.setObjectName("RecordLoad")
        RecordLoad.resize(400, 300)
        RecordLoad.setMinimumSize(QtCore.QSize(400, 300))
        RecordLoad.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("e:\\peng\\PythonProjects\\Sk_recorder\\ui\\../img/all.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RecordLoad.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(RecordLoad)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 61))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(RecordLoad)
        self.label.setGeometry(QtCore.QRect(10, 10, 261, 81))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(RecordLoad)
        self.textBrowser.setGeometry(QtCore.QRect(0, 101, 400, 199))
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(RecordLoad)
        self.buttonBox.accepted.connect(RecordLoad.accept) # type: ignore
        self.buttonBox.rejected.connect(RecordLoad.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(RecordLoad)

    def retranslateUi(self, RecordLoad):
        _translate = QtCore.QCoreApplication.translate
        RecordLoad.setWindowTitle(_translate("RecordLoad", "录制提示"))
        self.label.setText(_translate("RecordLoad", "<html><head/><body><p><span style=\" font-size:12pt;\">点击OK后开始录制, 录制过程中按下</span></p><p><span style=\" font-size:12pt;\">q键完成录制,下方为录制日志</span></p></body></html>"))
