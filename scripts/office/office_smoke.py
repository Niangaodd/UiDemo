# -*- encoding=utf8 -*-
__author__ = "Ashe Li"
__title__ = "政务大厅冒烟测试"

import sys
import random

sys.path.append(r"H:\Uiauto_demo")
from airtest.core.api import *
from airtest.report.report import simple_report, LogToHtml
from lib import public_using
from lib.general_operation import *

print("start...")


# if not cli_setup():
#     auto_setup(__file__, logdir=True, devices=["android:///"])


class HandleOffice():
    def __init__(self):
        self.enter_office()
        #         self.test_collect()
        self.test_office()
        self.close_office_to_home()

    def enter_office(self):
        touch(Template(r"tpl1742187921544.png", record_pos=(0.079, -0.212), resolution=(1260, 2720)))

    def test_collect(self):
        touch(wait(Template(r"tpl1742187981288.png", record_pos=(0.017, 0.675), resolution=(1260, 2720))))
        self.aotu_collect("gold", "food", "solider")
        touch((0.5, 0.15))  # 关闭征收弹框

    def aotu_collect(self, *args):
        """
        自动点击征收，直到征收全部
        :param args: 接收任意数量的参数，判断当前要征收的类型
        :return ：None
        """
        for i in args:
            while True:
                if i == "gold":
                    #                     touch(Template(r"tpl1742188082092.png", target_pos=8, record_pos=(0.221, -0.27), resolution=(1260, 2720)))
                    touch((0.70, 0.39))
                elif i == "food":
                    #                     touch(Template(r"tpl1742188304985.png", target_pos=8, record_pos=(0.218, 0.048), resolution=(1260, 2720)))
                    touch((0.70, 0.53))
                elif i == "solider":
                    #                     touch(Template(r"tpl1742188319487.png", target_pos=8, record_pos=(0.221, 0.349), resolution=(1260, 2720)))
                    touch((0.70, 0.69))
                if exists(Template(r"tpl1742188161220.png", record_pos=(0.382, -0.5), resolution=(1260, 2720))):
                    touch((0.5, 0.15))  # 关闭道具获取途径弹框
                    break

    def test_office(self):
        sleep(1)
        touch(wait(Template(r"tpl1742189189211.png", record_pos=(-0.304, -0.04), resolution=(1260, 2720))), times=2)
        options = [(0.45, 0.63), (0.45, 0.70)]
        while True:
            """随机点击选项一或选项二、每次点击后判断是否道具不足，处理所有政务后，关闭弹框"""
            option = random.choice(options)
            touch(option)
            if exists(Template(r"tpl1742189883221.png", record_pos=(0.009, -0.189), resolution=(1260, 2720))):
                touch((0.5, 0.15))  # 关闭道具获取途径弹框
                break
        touch((0.5, 0.15))  # 关闭政务弹框

    def close_office_to_home(self):
        touch(wait(Template(r"tpl1742189582944.png", record_pos=(-0.431, -0.86), resolution=(1260, 2720))))
        # 判断一下，是否存在拍脸弹框？
        public_using.close_face_window()


if __name__ == "__main__":
    try:
        HandleOffice()
    finally:
        log_dir = GeneralOperation.get_device_and_logdir()
        # 生成测试报告
        simple_report(__file__, logpath=log_dir, logfile="log.txt", output=os.path.join(log_dir, f"log.html"))
        # h1 = LogToHtml(script_root=__file__, log_root=log_dir,static_root=r"D:\static",
        #                export_dir=log_dir, logfile=os.path.join(log_dir,f"log.txt"), lang='zh',
        #                plugins=None)
        # h1.report()

#powershell运行脚本如下
#$env:LOG_DIR="H:\Uiauto_demo\scripts\office\log\HW_mate60_pro";airtest run H:\Uiauto_demo\scripts\office\office_smoke.py --device "android://127.0.0.1:5037/192.168.110.175:55555" --log "H:\Uiauto_demo\scripts\office\log\HW_mate60_pro";