# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Skyler

import wave
import sys
import threading
from os import remove,mkdir,listdir
from os.path import exists,splitext,basename,join
from datetime import datetime
from time import sleep
from shutil import rmtree
import pyaudio
from PIL import ImageGrab
from numpy import array
import cv2
from moviepy.editor import AudioFileClip, VideoFileClip, CompositeVideoClip
import json
from pynput import keyboard

CHUNK_sIZE = 1024
CHANNELS = 2
FORMAT = pyaudio.paInt16
RATE = 48000
allowRecording = True

with open('settings.json') as f:
    config = json.load(f)

def record_audio():
    p= pyaudio.PyAudio()
    # event.wait()
    sleep(3)
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=4,#立体混音，具体选哪个根据需要选择
                    frames_per_buffer = CHUNK_sIZE)
    wf = wave.open(audio_filename,'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    while allowRecording:
        # 从录音设备读取数据，直接写入wav文件
        data = stream.read(CHUNK_sIZE)
        wf.writeframes(data)
    wf.close()
    stream.stop_stream()
    stream.close()
    p.terminate()

def record_screen(r_size=None):
    # 录制屏幕
    im = ImageGrab.grab(r_size)
    video =cv2.VideoWriter(screen_video_filename,
                           cv2.VideoWriter_fourcc(*'XVID'),
                           25,im.size) #帧速和视频宽度、高度
    while allowRecording:
        im = ImageGrab.grab(r_size)
        im = cv2.cvtColor(array(im),cv2.COLOR_RGB2BGR)
        video.write(im)
    video.release()


def on_press(key):
    """监听按下键盘"""
    try:
        key_char = key.char
        if key_char == 'q':
            return False
    except AttributeError:
        pass


if __name__ == '__main__':
    print("按下q键停止完成录制")
    now = str(datetime.now())[:19].replace(':','_')
    audio_filename = f"{config['record_save_path']}/{now}.mp3"
    webcam_video_filename = f"{config['record_save_path']}/t{now}.avi"
    screen_video_filename = f"{config['record_save_path']}/tt{now}.avi"
    video_filename = f"{config['record_save_path']}/{now}.avi"

    #创建两个线程，分别录音和录屏
    if sys.argv[1] == 'full':
        t2 = threading.Thread(target=record_screen)
    elif sys.argv[1] == 'part':
        t2 = threading.Thread(target=record_screen, args=(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]))

    t1 = threading.Thread(target=record_audio)

    event = threading.Event()
    event.clear()
    for t in (t1,t2):
        t.start()
    # 等待摄像头准保好，开始录制
    # event.wait()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    allowRecording = False
    for i in (t1,t2):
        t.join()

    #把录制的视频和音频合成视频文件
    audio = AudioFileClip(audio_filename)
    video1 = VideoFileClip(screen_video_filename)
    ratio1 = audio.duration / video1.duration
    video1 = (video1.fl_time(lambda t: t/ratio1,apply_to=['video'])\
                .set_end(audio.duration))

    video = CompositeVideoClip([video1]).set_audio(audio)
    video.write_videofile(video_filename,codec= 'libx264',fps = 25)

    remove(audio_filename)
    remove(screen_video_filename)
