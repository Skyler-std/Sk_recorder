# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Skyler
import os
import sys
from time import sleep, strftime
from json import load

import pyperclip
from PIL import ImageGrab, Image
from log import add_log


class Clip:
    def __init__(self):
        with open('settings.json') as f:
            self.config = load(f)

    def get_now(self):
        """获取当前时间"""
        now = strftime('%Y-%m-%d %H.%M.%S')
        return now

    def get_clip_str(self):
        """获取文字剪切板"""
        text = pyperclip.paste()
        return text

    def get_clip_img(self):
        """获取图片剪切板"""
        im = ImageGrab.grabclipboard()
        if isinstance(im, Image.Image):
            return im

    def save_clip(self, content, save_type):
        """
        保存剪切板内容
        save_type为'str', 'img'中的一个
        """
        if save_type == 'str':
            file = self.config['cp_save_path'] + '/' + self.get_now() + '.txt'
            with open(file, 'w') as f:
                f.write(content)
        elif save_type == 'img':
            if content != None:
                add_log("Saving clip image")
                content.save(self.config['cp_save_path'] + '/' + self.get_now() + '.jpg')
                add_log("Save successful")


def clip_main():
    """主程序"""
    with open('program_position_cp.txt', 'w') as f:
        f.write(os.path.abspath(sys.argv[0]))
    my_clip = Clip()
    clip_text_old = None
    clip_img_old = None
    while True:
        clip_text = my_clip.get_clip_str()
        clip_img = my_clip.get_clip_img()
        if (clip_text != None) and (clip_text != clip_text_old):
            my_clip.save_clip(clip_text, 'str')
        if (clip_img != None) and (clip_img != clip_img_old):
            my_clip.save_clip(clip_img, 'img')
        clip_text_old = clip_text
        clip_img_old = clip_img
        sleep(0.1)


if __name__ == '__main__':
    clip_main()
