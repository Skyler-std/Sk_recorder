# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Skyler
from win32api import GetSystemMetrics
import pyautogui as pg
from PIL import ImageGrab

from json import load
from time import strftime
import sys


def get_now():
    """获取当前时间"""
    now = strftime('%Y-%m-%d %H.%M.%S')
    return now


def full_shot(save_path):
    """全屏截图"""
    img = ImageGrab.grab()
    img.save(save_path + '/' + get_now() + '.jpg')


def part_shot(save_path, b_x, b_y, e_x, e_y):
    """框选截图"""
    b_x = int(b_x)
    b_y = int(b_y)
    e_x = int(e_x)
    e_y = int(e_y)
    img = ImageGrab.grab((b_x, b_y, e_x, e_y))
    img.save(save_path + '/' + get_now() + '.jpg')


def run_shot():
    """主程序"""
    with open('settings.json') as f:
        config = load(f)
    save_Path = config['shot_save_path']

    if sys.argv[1] == 'full':
        full_shot(save_Path)
    elif sys.argv[1] == 'part':
        part_shot(save_Path, sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])


if __name__ == '__main__':
    run_shot()
