import sys

sys.path.append(r"H:\Uiauto_demo")
from airtest.core.api import *


def close_face_window():
    if exists(Template(r"tpl1741695450607.png", record_pos=(-0.011, -0.27),
                       resolution=(1260, 2720))):
        touch((0.5, 0.08))
    else:
        while True:  # 如果存在拍脸弹窗,点击关闭(可能有多个弹窗)
            if exists(Template(r"tpl1741685805003.png", record_pos=(0.447, -0.797),
                               resolution=(1260, 2720))):
                touch(Template(r"tpl1741685813499.png", record_pos=(0.441, -0.792),
                               resolution=(1260, 2720)))
                sleep(0.5)
            else:
                break


def touch_back():
    """点击左上角的返回按钮"""
    touch(wait(Template(r"tpl1741691361234.png", record_pos=(0.03, 0.08),
                        resolution=(1260, 2720))),duration=0.1)
