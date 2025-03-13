# -*- encoding=utf8 -*-
__author__ = "Ashe Li"
__title__ = '启动脚本'
__desc__ = '''启动游戏-》点击start-》进入功能列表页'''

import sys

from lib.general_operation import GeneralOperation

sys.path.append(r'H:\Uiauto_demo')
from airtest.core.api import *
from airtest.core.android.recorder import *
from airtest.core.android.adb import *
auto_setup(__file__, logdir=True)


def enter_homepage():
    touch(Template(r"tpl1741667494549.png", record_pos=(0.073, -0.142), resolution=(1920, 1080)))
    sleep(5)
    start = Template(r"tpl1741601378227.png", record_pos=(0.026, -0.065), resolution=(2720, 1260))
    print('start：', start)

    wait(start)
    assert_exists(start, "成功进入启动界面")
    touch(start)
    assert_exists(Template(r"tpl1741601434540.png", record_pos=(-0.195, -0.019), resolution=(2720, 1260)),
                  "成功进入功能列表")

def click_back():
    touch(Template(r"tpl1741678577432.png", record_pos=(-0.322, 0.166), resolution=(2720, 1260)))


# #实例化recorder
# recorder = Recorder(adb)
# #开始录屏，最大录屏默认1800秒

if __name__ == "__main__":
    adb = ADB(serialno="23E0224711011260")
    recorder = Recorder(adb)
    recorder.start_recording()
    enter_homepage()
    recorder.stop_recording(GeneralOperation.build_record_path(__file__))

