# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from log import add_log

import os
from json import dump, load
from threading import Thread


class Ui_SettingWindow(object):
    def setupUi(self, SettingWindow):
        SettingWindow.setObjectName("SettingWindow")
        SettingWindow.resize(365, 346)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        SettingWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/all.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SettingWindow.setWindowIcon(icon)
        self.RecordTimeEdit = QtWidgets.QTimeEdit(SettingWindow)
        self.RecordTimeEdit.setEnabled(False)
        self.RecordTimeEdit.setGeometry(QtCore.QRect(220, 10, 121, 41))
        self.RecordTimeEdit.setObjectName("RecordTimeEdit")
        self.RecordTimeEnableButton = QtWidgets.QCommandLinkButton(SettingWindow)
        self.RecordTimeEnableButton.setGeometry(QtCore.QRect(10, 10, 185, 41))
        self.RecordTimeEnableButton.setObjectName("RecordTimeEnableButton")
        self.RecordTimeDisableButton = QtWidgets.QCommandLinkButton(SettingWindow)
        self.RecordTimeDisableButton.setEnabled(False)
        self.RecordTimeDisableButton.setGeometry(QtCore.QRect(10, 60, 185, 41))
        self.RecordTimeDisableButton.setObjectName("RecordTimeDisableButton")
        self.RecordTimeOkButton = QtWidgets.QPushButton(SettingWindow)
        self.RecordTimeOkButton.setGeometry(QtCore.QRect(220, 60, 121, 41))
        self.RecordTimeOkButton.setObjectName("RecordTimeOkButton")
        self.RecordTimeOkButton.setEnabled(False)
        self.ClipPathButton = QtWidgets.QPushButton(SettingWindow)
        self.ClipPathButton.setGeometry(QtCore.QRect(10, 280, 161, 51))
        self.ClipPathButton.setObjectName("ClipPathButton")
        self.textBrowser = QtWidgets.QTextBrowser(SettingWindow)
        self.textBrowser.setGeometry(QtCore.QRect(10, 170, 331, 101))
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(SettingWindow)
        self.label.setGeometry(QtCore.QRect(13, 111, 321, 41))
        self.label.setObjectName("label")
        self.SettingExitButton = QtWidgets.QPushButton(SettingWindow)
        self.SettingExitButton.setGeometry(QtCore.QRect(194, 282, 141, 51))
        self.SettingExitButton.setObjectName("SettingExitButton")

        # 初始化读取配置
        if os.path.exists('settings.json'):
            with open('settings.json') as f:
                config = load(f)
            # 控件启用
            if config['set_enable']:
                self.RecordTimeEnableButton.setEnabled(False)
                self.RecordTimeDisableButton.setEnabled(True)
                self.RecordTimeEdit.setEnabled(True)
                self.RecordTimeOkButton.setEnabled(True)
            elif not config['set_enable']:
                self.RecordTimeEnableButton.setEnabled(True)
                self.RecordTimeDisableButton.setEnabled(False)
                self.RecordTimeEdit.setEnabled(False)
                self.RecordTimeOkButton.setEnabled(False)
            # 数值设定
            if ('set_hour' in config) and ('set_minute' in config):
                format_time = QtCore.QTime(config['set_hour'], config['set_minute'])
                self.RecordTimeEdit.setTime(format_time)
            if 'cp_save_path' in config:
                self.textBrowser.append(config['cp_save_path'])
            elif 'cp_save_path' not in config:
                self.textBrowser.append("C:/slip")

        # 信号槽函数连接
        self.SettingExitButton.clicked.connect(self.stbt)
        self.RecordTimeEnableButton.clicked.connect(self.enableF)
        self.RecordTimeDisableButton.clicked.connect(self.disableF)
        self.RecordTimeOkButton.clicked.connect(self.tm_ok)
        self.ClipPathButton.clicked.connect(self.cp_choose)

        self.retranslateUi(SettingWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingWindow)

    def cp_choose(self):
        """选择剪切板保存位置"""
        file = 'settings.json'
        file_dialog = QtWidgets.QFileDialog.getExistingDirectory(None, "选择保存位置", 'C:/slip')
        if file_dialog != '':
            add_log("Reading setting")
            # 导入保存配置
            with open(file) as f:
                setting = load(f)
            add_log("Reading successful")
            setting['cp_save_path'] = file_dialog
            add_log("Updating config")
            with open(file, 'w') as f:
                dump(setting, f, indent=4)
            add_log("Update successful")
            self.textBrowser.clear()
            self.textBrowser.append(file_dialog)

    def tm_ok(self):
        """确认录制时间"""
        def tm_f():
            set_hour = self.RecordTimeEdit.time().hour()
            set_minute = self.RecordTimeEdit.time().minute()
            add_log(f"Setting hour: {set_hour}")
            add_log(f"Setting minute: {set_minute}")
            add_log("Start to write setting")
            file = 'settings.json'
            if not os.path.exists(file):
                set_dict = {'set_hour': set_hour, 'set_minute': set_minute, 'set_enable': True,
                            'cp_save_position': 'C:/slip'}
                with open(file, 'w') as f:
                    dump(set_dict, f, indent=4)
            elif os.path.exists(file):
                with open(file) as f:
                    config = load(f)
                config['set_hour'] = set_hour
                config['set_minute'] = set_minute
                config['set_enable'] = True
                with open(file, 'w') as f:
                    dump(config, f, indent=4)
            add_log("Write successful")
        tm_th = Thread(target=tm_f, daemon=True)
        tm_th.start()

    def stbt(self):
        """应用并退出按钮点击触发事件"""
        SettingWindow.close()

    def enableF(self):
        """启用自定义录屏时间"""
        self.RecordTimeEnableButton.setEnabled(False)
        self.RecordTimeDisableButton.setEnabled(True)
        self.RecordTimeEdit.setEnabled(True)
        self.RecordTimeOkButton.setEnabled(True)

    def disableF(self):
        """禁用自定义录屏时间"""
        self.RecordTimeDisableButton.setEnabled(False)
        self.RecordTimeEnableButton.setEnabled(True)
        self.RecordTimeEdit.setEnabled(False)
        self.RecordTimeOkButton.setEnabled(False)
        file = 'settings.json'
        add_log("Starting to writing setting disable")
        with open(file) as f:
            setting = load(f)
        setting['set_enable'] = False
        with open(file, 'w') as f:
            dump(setting, f, indent=4)
        add_log("Write successful")

    def retranslateUi(self, SettingWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingWindow.setWindowTitle(_translate("SettingWindow", "总体设置"))
        self.RecordTimeEnableButton.setText(_translate("SettingWindow", "启用自定义录屏时长"))
        self.RecordTimeDisableButton.setText(_translate("SettingWindow", "禁用自定义录屏时长"))
        self.RecordTimeOkButton.setText(_translate("SettingWindow", "确定"))
        self.ClipPathButton.setText(_translate("SettingWindow", "设置剪切板保存位置"))
        self.label.setText(_translate("SettingWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">剪切板设定保存位置(为空则为缺省值)</span></p></body></html>"))
        self.SettingExitButton.setText(_translate("SettingWindow", "应用并退出"))


SettingWindow = QtWidgets.QWidget()
ui_setting = Ui_SettingWindow()
ui_setting.setupUi(SettingWindow)
