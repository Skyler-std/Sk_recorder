# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Skyler

from subprocess import call
from threading import Thread
from time import strftime


def add_log(content):
    """添加日志"""
    def aadd():
        with open('run.log', 'a') as f:
            f.write(strftime('[%H:%M:%S]') + '\n' + content + '\n')
    aadd_th = Thread(target=aadd, daemon=True)
    aadd_th.start()


def rm_log():
    """删除日志"""
    def rrmm():
        with open('run.log', 'w') as f:
            pass
    rrmm_th = Thread(target=rrmm, daemon=True)
    rrmm_th.start()


def view_log():
    """查看日志"""
    def vvii():
        CREATE_NO_WINDOW = 0x08000000
        call('notepad.exe run.log', creationflags=CREATE_NO_WINDOW)
    vvii_th = Thread(target=vvii, daemon=True)
    vvii_th.start()
