# -*- encoding=utf8 -*-
__author__ = "Ashe Li"
__title__ = '启动脚本'
__desc__ = '''启动游戏-》点击start-》进入功能列表页'''

import sys

sys.path.append(r'H:\Uiauto_demo')
from airtest.core.api import *
from airtest.core.android.recorder import *
from airtest.core.android.adb import *

def enter_homepage():
    start_app("com.NetEase")
    sleep(5)
    start = Template(r"tpl1741601378227.png", record_pos=(0.026, -0.065), resolution=(2720, 1260))

    wait(start)
    assert_exists(start, "成功进入启动界面")
    touch(start)
    assert_exists(Template(r"tpl1741601434540.png", record_pos=(-0.195, -0.019), resolution=(2720, 1260)),
                  "成功进入功能列表")

def click_back():
    touch(Template(r"tpl1741678577432.png", record_pos=(-0.322, 0.166), resolution=(2720, 1260)))



if __name__ == "__main__":
    adb = ADB(serialno="23E0224711011260")
    recorder = Recorder(adb)
    recorder.start_recording()
    enter_homepage()
    recorder.stop_recording(GeneralOperation.build_record_path(__file__))


