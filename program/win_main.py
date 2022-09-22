# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import sys
import os
import subprocess
from json import load, dump
from threading import Thread
from shutil import copyfile

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
import pynput.mouse as pm
import cv2
from log import rm_log, view_log, add_log


CREATE_NO_WINDOW = 0x08000000


class Ui_MainWindow(object):
    def __init__(self):
        self.x = []
        self.y = []
        self.click_time = 0
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 618)
        MainWindow.setMinimumSize(QtCore.QSize(622, 618))
        MainWindow.setMaximumSize(QtCore.QSize(622, 618))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/all.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SshotLabel = QtWidgets.QLabel(self.centralwidget)
        self.SshotLabel.setGeometry(QtCore.QRect(10, 70, 141, 41))
        self.SshotLabel.setObjectName("SshotLabel")
        self.SshotFileChoiceButton = QtWidgets.QPushButton(self.centralwidget)
        self.SshotFileChoiceButton.setGeometry(QtCore.QRect(160, 70, 81, 41))
        self.SshotFileChoiceButton.setObjectName("SshotFileChoiceButton")
        self.SshotAllGetButton = QtWidgets.QPushButton(self.centralwidget)
        self.SshotAllGetButton.setGeometry(QtCore.QRect(10, 120, 81, 41))
        self.SshotAllGetButton.setObjectName("SshotAllGetButton")
        self.SshotPartGetButton = QtWidgets.QPushButton(self.centralwidget)
        self.SshotPartGetButton.setGeometry(QtCore.QRect(100, 120, 81, 41))
        self.SshotPartGetButton.setObjectName("SshotPartGetButton")
        self.SshotOpenSaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SshotOpenSaveButton.setGeometry(QtCore.QRect(190, 120, 141, 41))
        self.SshotOpenSaveButton.setObjectName("SshotOpenSaveButton")
        self.SshotSaveLabel = QtWidgets.QLabel(self.centralwidget)
        self.SshotSaveLabel.setGeometry(QtCore.QRect(260, 70, 71, 41))
        self.SshotSaveLabel.setObjectName("SshotSaveLabel")
        self.SshotTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.SshotTextBrowser.setGeometry(QtCore.QRect(340, 70, 271, 91))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.SshotTextBrowser.setFont(font)
        self.SshotTextBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.SshotTextBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SshotTextBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.SshotTextBrowser.setObjectName("SshotTextBrowser")
        self.SshotTitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.SshotTitleLabel.setGeometry(QtCore.QRect(0, 0, 621, 61))
        self.SshotTitleLabel.setObjectName("SshotTitleLabel")
        self.SshotgraphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.SshotgraphicsView.setGeometry(QtCore.QRect(0, 0, 621, 61))
        self.SshotgraphicsView.setObjectName("SshotgraphicsView")
        self.RecordTitlegraphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.RecordTitlegraphicsView.setGeometry(QtCore.QRect(0, 170, 621, 61))
        self.RecordTitlegraphicsView.setObjectName("RecordTitlegraphicsView")
        self.RecordTitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.RecordTitleLabel.setGeometry(QtCore.QRect(0, 170, 621, 61))
        self.RecordTitleLabel.setObjectName("RecordTitleLabel")
        self.RecordTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.RecordTextBrowser.setGeometry(QtCore.QRect(340, 240, 271, 91))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.RecordTextBrowser.setFont(font)
        self.RecordTextBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.RecordTextBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RecordTextBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.RecordTextBrowser.setObjectName("RecordTextBrowser")
        self.RecordSaveLable = QtWidgets.QLabel(self.centralwidget)
        self.RecordSaveLable.setGeometry(QtCore.QRect(260, 240, 71, 41))
        self.RecordSaveLable.setObjectName("RecordSaveLable")
        self.RecordOpenSaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.RecordOpenSaveButton.setGeometry(QtCore.QRect(190, 290, 141, 41))
        self.RecordOpenSaveButton.setObjectName("RecordOpenSaveButton")
        self.RecordLabel = QtWidgets.QLabel(self.centralwidget)
        self.RecordLabel.setGeometry(QtCore.QRect(10, 240, 141, 41))
        self.RecordLabel.setObjectName("RecordLabel")
        self.RecordPartGetButton = QtWidgets.QPushButton(self.centralwidget)
        self.RecordPartGetButton.setGeometry(QtCore.QRect(100, 290, 81, 41))
        self.RecordPartGetButton.setObjectName("RecordPartGetButton")
        self.RecordFileChoiceButton = QtWidgets.QPushButton(self.centralwidget)
        self.RecordFileChoiceButton.setGeometry(QtCore.QRect(160, 240, 81, 41))
        self.RecordFileChoiceButton.setObjectName("RecordFileChoiceButton")
        self.RecordAllGetButton = QtWidgets.QPushButton(self.centralwidget)
        self.RecordAllGetButton.setGeometry(QtCore.QRect(10, 290, 81, 41))
        self.RecordAllGetButton.setObjectName("RecordAllGetButton")
        self.SshotViewDisplay = QtWidgets.QGraphicsView(self.centralwidget)
        self.SshotViewDisplay.setGeometry(QtCore.QRect(10, 390, 200, 171))
        self.SshotViewDisplay.setObjectName("SshotViewDisplay")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(420, 520, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ExitButton.setFont(font)
        self.ExitButton.setObjectName("ExitButton")
        self.SshotViewLabel = QtWidgets.QLabel(self.centralwidget)
        self.SshotViewLabel.setGeometry(QtCore.QRect(10, 340, 201, 41))
        self.SshotViewLabel.setObjectName("SshotViewLabel")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 340, 201, 41))
        self.graphicsView.setObjectName("graphicsView")
        self.CpEnableButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.CpEnableButton.setEnabled(True)
        self.CpEnableButton.setGeometry(QtCore.QRect(230, 340, 181, 41))
        self.CpEnableButton.setObjectName("CpEnableButton")
        self.CpDisableButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.CpDisableButton.setEnabled(False)
        self.CpDisableButton.setGeometry(QtCore.QRect(230, 390, 181, 41))
        self.CpDisableButton.setObjectName("CpDisableButton")
        self.CpHelpLabel = QtWidgets.QLabel(self.centralwidget)
        self.CpHelpLabel.setGeometry(QtCore.QRect(420, 340, 191, 171))
        self.CpHelpLabel.setObjectName("CpHelpLabel")
        self.CpHelpBg = QtWidgets.QGraphicsView(self.centralwidget)
        self.CpHelpBg.setGeometry(QtCore.QRect(420, 340, 191, 171))
        self.CpHelpBg.setObjectName("CpHelpBg")
        self.CpAutoRunCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.CpAutoRunCheckBox.setGeometry(QtCore.QRect(240, 440, 123, 31))
        self.CpAutoRunCheckBox.setObjectName("CpAutoRunCheckBox")
        self.AutoRunCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.AutoRunCheckBox.setGeometry(QtCore.QRect(240, 490, 123, 31))
        self.AutoRunCheckBox.setObjectName("AutoRunCheckBox")
        self.CpHelpBg.raise_()
        self.graphicsView.raise_()
        self.SshotgraphicsView.raise_()
        self.SshotLabel.raise_()
        self.SshotFileChoiceButton.raise_()
        self.SshotAllGetButton.raise_()
        self.SshotPartGetButton.raise_()
        self.SshotOpenSaveButton.raise_()
        self.SshotSaveLabel.raise_()
        self.SshotTextBrowser.raise_()
        self.SshotTitleLabel.raise_()
        self.RecordTitlegraphicsView.raise_()
        self.RecordTitleLabel.raise_()
        self.RecordTextBrowser.raise_()
        self.RecordSaveLable.raise_()
        self.RecordOpenSaveButton.raise_()
        self.RecordLabel.raise_()
        self.RecordPartGetButton.raise_()
        self.RecordFileChoiceButton.raise_()
        self.RecordAllGetButton.raise_()
        self.SshotViewDisplay.raise_()
        self.ExitButton.raise_()
        self.SshotViewLabel.raise_()
        self.CpEnableButton.raise_()
        self.CpDisableButton.raise_()
        self.CpHelpLabel.raise_()
        self.CpAutoRunCheckBox.raise_()
        self.AutoRunCheckBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 23))
        self.menubar.setObjectName("menubar")
        self.menu_setting = QtWidgets.QMenu(self.menubar)
        self.menu_setting.setObjectName("menu_setting")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_log = QtWidgets.QMenu(self.menubar)
        self.menu_log.setObjectName("menu_log")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsettings = QtWidgets.QAction(MainWindow)
        self.actionsettings.setObjectName("actionsettings")
        self.actionDonate = QtWidgets.QAction(MainWindow)
        self.actionDonate.setObjectName("actionDonate")
        self.actionViewLog = QtWidgets.QAction(MainWindow)
        self.actionViewLog.setObjectName("actionViewLog")
        self.actionRmLog = QtWidgets.QAction(MainWindow)
        self.actionRmLog.setObjectName("actionRmLog")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.menu_setting.addAction(self.actionsettings)
        self.menu_help.addAction(self.action_about)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.actionDonate)
        self.menu_log.addAction(self.actionViewLog)
        self.menu_log.addAction(self.actionRmLog)
        self.menubar.addAction(self.menu_setting.menuAction())
        self.menubar.addAction(self.menu_log.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)

        # 初始化显示
        with open('settings.json') as f:
            config = load(f)
        self.SshotTextBrowser.append(config['shot_save_path'])
        self.RecordTextBrowser.append(config['record_save_path'])
        if config['cp_enable']:
            self.CpDisableButton.setEnabled(True)
            self.CpEnableButton.setEnabled(False)
        if config['auto_run']:
            self.AutoRunCheckBox.setChecked(True)
        if config['auto_run_cp']:
            self.CpAutoRunCheckBox.setChecked(True)

        def main_exit():
            """退出程序"""
            MainWindow.close()
            add_log("#######Program finished#######")
            sys.exit(0)

        # ===============================信号连接槽函数================================
        self.ExitButton.clicked.connect(main_exit)
        self.action_about.triggered.connect(self.run_about)
        self.actionDonate.triggered.connect(self.run_donate)
        self.actionsettings.triggered.connect(self.run_setting)
        self.actionViewLog.triggered.connect(view_log)
        self.actionRmLog.triggered.connect(rm_log)
        self.SshotFileChoiceButton.clicked.connect(self.shot_file_choice)
        self.SshotOpenSaveButton.clicked.connect(self.shot_open_folder)
        self.RecordFileChoiceButton.clicked.connect(self.record_file_choice)
        self.RecordOpenSaveButton.clicked.connect(self.record_open_folder)
        self.CpEnableButton.clicked.connect(self.cp_enable)
        self.CpDisableButton.clicked.connect(self.cp_disable)
        self.AutoRunCheckBox.clicked.connect(self.auto_run)
        self.CpAutoRunCheckBox.clicked.connect(self.auto_run_cp)
        self.SshotAllGetButton.clicked.connect(self.shot_all_get)
        self.SshotPartGetButton.clicked.connect(self.shot_part_get)
        self.RecordAllGetButton.clicked.connect(self.record_all_get)
        self.RecordPartGetButton.clicked.connect(self.record_part_get)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def record_all_get(self):
        """全屏录屏"""
        def r_th_f():
            subprocess.call('record.exe full')
        r_th = Thread(target=r_th_f, daemon=True)
        r_th.start()
    
    
    def record_part_get(self):
        """框选录屏"""
        def listener(x, y, button, pressed):
            if pressed and (button == pm.Button.left):
                add_log("Button left detected")
                self.click_time += 1
                if self.click_time < 3:
                    self.x.append(x)
                    self.y.append(y)
                    add_log(f"Current value x is {str(self.x)}")
                    add_log(f"Current value y is {str(self.y)}")
                elif self.click_time >= 3:
                    return False

        def listen_tth_f():
            with pm.Listener(on_click=listener) as pmlistener:
                pmlistener.join()

        def get_tth_f():
            while True:
                if len(self.x) == 2 and len(self.y) == 2:
                    add_log("Start to part record")
                    add_log("Running f-record.exe part {self.x[0]} {self.y[0]} {self.x[1]} {self.y[1]}")
                    subprocess.call(f'record.exe part {self.x[0]} {self.y[0]} {self.x[1]} {self.y[1]}')
                    add_log("Run successful, waiting to save and reset value")
                    self.x.clear()
                    self.y.clear()
                    self.click_time = 0
                    add_log("Ending threads")
                    break
        add_log("Setting threads to part shot")
        listen_tth = Thread(target=listen_tth_f, daemon=True)
        get_tth = Thread(target=get_tth_f, daemon=True)
        add_log("Starting threads")
        listen_tth.start()
        get_tth.start()
        add_log("Start successful")
            


    def shot_part_get(self):
        """框选截图"""
        from win_shot_part_help import SshotPartGetWindow
        SshotPartGetWindow.show()


    def shot_all_get(self):
        """全屏截图"""
        def shot_all_f():
            subprocess.call('shot.exe full')
        shot_all_th = Thread(target=shot_all_f, daemon=True)
        shot_all_th.start()


    def auto_run_cp(self):
        """自启剪切板"""
        with open('settings.json') as f:
            config = load(f)
        status = self.CpAutoRunCheckBox.isChecked()
        auto_path = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp'
        if status:
            config['auto_run_cp'] = True
            add_log("Starting to write auto run clip config")
            with open('settings.json', 'w') as f:
                dump(config, f, indent=4)
            add_log("Adding successful")
            add_log("Applying config")
            add_log("Creating link")
            def app_cp_f():
                # 创建快捷方式
                with open('program_position_cp.txt') as f:
                    p_path = f.readlines()[0]
                while '/' in p_path:
                    p_path = p_path.replace('/', '\\')
                if os.path.exists(f'{auto_path}/Sk_recorder_clip.lnk'):
                    os.remove(f'{auto_path}/Sk_recorder_clip.lnk')
                os.system(f'mklink Sk_recorder_clip.lnk {p_path}')
                copyfile('Sk_recorder_clip.lnk', auto_path + '/Sk_recorder_clip.lnk', follow_symlinks=False)
                subprocess.call('clip.exe', creationflags=CREATE_NO_WINDOW)
            app_cp_th = Thread(target=app_cp_f, daemon=True)
            app_cp_th.start()
        elif not status:
            config['auto_run_cp'] = False
            add_log("Starting to write auto run clip config")
            with open('settings.json', 'w') as f:
                dump(config, f, indent=4)
            add_log("Adding successful")
            add_log("Applying config")
            add_log("Deleting link")

            def app_ff():
                # 移除快捷方式
                try:
                    os.remove(f'{auto_path}/Sk_recorder_clip.lnk')
                except:
                    add_log("Error occurs while deleting lnk")
                os.system('taskkill /f /im clip.exe')

            app_tth = Thread(target=app_ff, daemon=True)
            app_tth.start()


    def auto_run(self):
        """开机自启本软件"""
        with open('settings.json') as f:
            config = load(f)
        status = self.AutoRunCheckBox.isChecked()
        auto_path = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp'
        if status:
            config['auto_run'] = True
            add_log("Starting to write auto run config")
            with open('settings.json', 'w') as f:
                dump(config, f, indent=4)
            add_log("Adding successful")
            add_log("Applying config")
            add_log("Creating link")
            def app_f():
                # 创建快捷方式
                with open('program_position.txt') as f:
                    p_path = f.readlines()[0]
                while '/' in p_path:
                    p_path = p_path.replace('/', '\\')
                os.system(f'mklink Sk_recorder.lnk {p_path}')
                if os.path.exists(f'{auto_path}/Sk_recorder.lnk'):
                    os.remove(f'{auto_path}/Sk_recorder.lnk')
                copyfile('Sk_recorder.lnk', auto_path + '/Sk_recorder.lnk', follow_symlinks=False)
            app_th = Thread(target=app_f, daemon=True)
            app_th.start()
        elif not status:
            config['auto_run'] = False
            add_log("Starting to write auto run config")
            with open('settings.json', 'w') as f:
                dump(config, f, indent=4)
            add_log("Adding successful")
            add_log("Applying config")
            add_log("Deleting link")

            def app_ff():
                # 移除快捷方式
                try:
                    os.remove(f'{auto_path}/Sk_recorder.lnk')
                except:
                    add_log("Error occurs while deleting lnk")

            app_tth = Thread(target=app_ff, daemon=True)
            app_tth.start()


    def cp_disable(self):
        """禁用剪切板功能"""
        self.CpEnableButton.setEnabled(True)
        self.CpDisableButton.setEnabled(False)
        add_log("Starting to disable clip")
        with open('settings.json') as f:
            config = load(f)
        config['cp_enable'] = False
        with open('settings.json', 'w') as f:
            dump(config, f, indent=4)
        add_log("Done!")
        def cp_kill_f():
            subprocess.call('taskkill /f /im clip.exe', creationflags=CREATE_NO_WINDOW)
        cp_kill_th = Thread(target=cp_kill_f, daemon=True)
        cp_kill_th.start()


    def cp_enable(self):
        """启用剪切板功能"""
        self.CpEnableButton.setEnabled(False)
        self.CpDisableButton.setEnabled(True)
        add_log("Starting to enable clip")
        with open('settings.json') as f:
            config = load(f)
        config['cp_enable'] = True
        with open('settings.json', 'w') as f:
            dump(config, f, indent=4)
        add_log("Done!")
        def cp_start_f():
            subprocess.call('clip.exe', creationflags=CREATE_NO_WINDOW)
        cp_start_th = Thread(target=cp_start_f, daemon=True)
        cp_start_th.start()


    def record_open_folder(self):
        """打开截图保存文件夹"""
        add_log("Loading setting")
        with open('settings.json') as f:
            config = load(f)
        config = config['record_save_path']
        add_log("Loading successful")
        while '/' in config:
            config = config.replace('/', '\\')
        def open_th_f():
            subprocess.call('explorer.exe ' + config, creationflags=CREATE_NO_WINDOW)
        open_th = Thread(target=open_th_f, daemon=True)
        add_log("Start to open folder")
        open_th.start()
        add_log("Thread create successful")


    def record_file_choice(self):
        """选择截屏保存位置"""
        save_dialog = QtWidgets.QFileDialog.getExistingDirectory(None, "选择保存位置", 'C:/rrecord')
        if save_dialog != '':
            with open('settings.json') as f:
                config = load(f)
            config['record_save_path'] = save_dialog
            with open('settings.json', 'w') as f:
                dump(config, f, indent=4)
            self.RecordTextBrowser.clear()
            self.RecordTextBrowser.append(save_dialog)


    def shot_open_folder(self):
        """打开截图保存文件夹"""
        with open('settings.json') as f:
            config = load(f)
        config = config['shot_save_path']
        while '/' in config:
            config = config.replace('/', '\\')
        def open_th_f():
            subprocess.call('explorer.exe ' + config, creationflags=CREATE_NO_WINDOW)
        open_th = Thread(target=open_th_f, daemon=True)
        open_th.start()


    def shot_file_choice(self):
        """选择截屏保存位置"""
        save_dialog = QtWidgets.QFileDialog.getExistingDirectory(None, "选择保存位置", 'C:/sshot')
        if save_dialog != '':
            with open('settings.json') as f:
                config = load(f)
            config['shot_save_path'] = save_dialog
            with open('settings.json', 'w') as f:
                dump(config, f, indent=4)
            self.SshotTextBrowser.clear()
            self.SshotTextBrowser.append(save_dialog)


    def run_about(self):
        """运行关于窗口"""
        add_log("Loading AboutWindow")
        from win_about import AboutWindow
        AboutWindow.show()
        add_log("Load successful")


    def run_donate(self):
        """运行捐赠窗口"""
        add_log("Loading DonateWindow")
        from win_donate import DonateWindow
        DonateWindow.show()
        add_log("Load successful")


    def run_setting(self):
        """运行设置窗口"""
        add_log("Loading SettingWindow")
        from win_setting import SettingWindow
        SettingWindow.show()
        add_log("Load successful")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sk_recorder(By: Skyler Sun)"))
        self.SshotLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#64ea3f;\">选择截图保存位置</span></p></body></html>"))
        self.SshotFileChoiceButton.setText(_translate("MainWindow", "浏览"))
        self.SshotAllGetButton.setText(_translate("MainWindow", "全屏"))
        self.SshotPartGetButton.setText(_translate("MainWindow", "框选"))
        self.SshotOpenSaveButton.setText(_translate("MainWindow", "打开保存位置"))
        self.SshotSaveLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#53c1ba;\">保存位置</span></p></body></html>"))
        self.SshotTitleLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">截屏功能区</span></p></body></html>"))
        self.RecordTitleLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">录屏功能区</span></p></body></html>"))
        self.RecordSaveLable.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#53c1ba;\">保存位置</span></p></body></html>"))
        self.RecordOpenSaveButton.setText(_translate("MainWindow", "打开保存位置"))
        self.RecordLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#64ea3f;\">选择截图保存位置</span></p></body></html>"))
        self.RecordPartGetButton.setText(_translate("MainWindow", "框选"))
        self.RecordFileChoiceButton.setText(_translate("MainWindow", "浏览"))
        self.RecordAllGetButton.setText(_translate("MainWindow", "全屏"))
        self.ExitButton.setText(_translate("MainWindow", "退出"))
        self.SshotViewLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">截屏预览</span></p></body></html>"))
        self.CpEnableButton.setText(_translate("MainWindow", "启用剪切板保存功能"))
        self.CpDisableButton.setText(_translate("MainWindow", "禁用剪切板保存功能"))
        self.CpHelpLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">当启用剪切板保存功能后</span></p><p><span style=\" font-size:11pt;\">剪切板默认保存C:\\slip</span></p><p><span style=\" font-size:11pt;\">复制文本会保存在txt文件</span></p><p><span style=\" font-size:11pt;\">若要更改相关设定</span></p><p><span style=\" font-size:11pt;\">菜单栏-&gt;设置-&gt;总体设置</span></p></body></html>"))
        self.CpAutoRunCheckBox.setText(_translate("MainWindow", "开机自启剪切板"))
        self.AutoRunCheckBox.setText(_translate("MainWindow", "开机自启本软件"))
        self.menu_setting.setTitle(_translate("MainWindow", "设置"))
        self.menu_help.setTitle(_translate("MainWindow", "帮助"))
        self.menu_log.setTitle(_translate("MainWindow", "日志"))
        self.actionsettings.setText(_translate("MainWindow", "总体设置"))
        self.actionsettings.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionDonate.setText(_translate("MainWindow", "捐赠"))
        self.actionViewLog.setText(_translate("MainWindow", "查看日志"))
        self.actionRmLog.setText(_translate("MainWindow", "删除日志"))
        self.action_about.setText(_translate("MainWindow", "关于"))
        self.action_about.setShortcut(_translate("MainWindow", "Ctrl+H"))
