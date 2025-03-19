# -*- encoding=utf8 -*-
__author__ = "Ashe Li"
__title__ = "完成第一步强制引导"
__desc__ = "从后宫引导-》领取第一个引导任务的奖励"

import sys
sys.path.append(r"H:\Uiauto_demo")
from config import casual
from airtest.core.api import *
from lib import public_using
from lib.general_operation import GeneralOperation
import logging
GeneralOperation.set_logging_config()

auto_setup(__file__, devices=["android:///"])

class MainStep:
    @staticmethod
    def test_timeline_guild():
        # print("main_step所在的目录",os.path.dirname(os.path.realpath(__file__)))
        # os.chdir(os.path.dirname(os.path.realpath(__file__)))
        continue_pos = wait(Template(r"tpl1742267210865.png", record_pos=(0.299, 0.922), resolution=(1080, 2400)))
        snapshot(msg="检查开场第一张timeline显示")
        touch(continue_pos)
        wait(Template(r"tpl1742267284740.png", record_pos=(-0.339, -0.936), resolution=(1080, 2400)), timeout=100)#等待对话剧情出现
        sleep(3)
        touch(casual)
        wait(Template(r"tpl1742267210865.png", record_pos=(0.299, 0.922), resolution=(1080, 2400)), timeout=100)
        touch(continue_pos)
        wait(Template(r"tpl1742267284740.png", record_pos=(-0.339, -0.936), resolution=(1080, 2400)), timeout=100)#等待对话剧情出现
        while True:#持续观看剧情，直到出现timeline
            touch(casual)
            if exists(Template(r"tpl1742267410427.png", record_pos=(0.23, 0.876), resolution=(1080, 2400))):
                break
        while True:#持续观看timeline,直到出现对话剧情
            touch(casual)
            if exists(Template(r"tpl1742268197895.png", record_pos=(0.242, -0.519), resolution=(1080, 2400))):#这个判断不对，改成国王
                break    
                
        while True:#持续观看剧情，直到出现取名弹框
            touch(casual)
            if exists(Template(r"tpl1742267528865.png", record_pos=(0.004, -0.299), resolution=(1080, 2400))):
                touch(Template(r"tpl1742267544544.png", record_pos=(-0.009, 0.027), resolution=(1080, 2400)))
                break    
        while True:#重新判断，否则上一段判断的太多了执行太久
            touch(casual)
            if exists(Template(r"tpl1742267601743.png", record_pos=(-0.231, -0.527), resolution=(1080, 2400)))  :#等待娜娜出现
                snapshot(msg="检查娜娜出场界面显示")
                break
        while True:#重新判断，否则上一段判断的太多了执行太久
            touch(casual)
            if exists(Template(r"tpl1742267690704.png", record_pos=(-0.389, -0.685), resolution=(1080, 2400)))  :#等待娜娜结婚界面
                snapshot(msg="检查娜娜结婚界面显示")
                break
        while True:#重新判断，否则上一段判断的太多了执行太久
            touch(casual)
            if exists(Template(r"tpl1742301250476.png", record_pos=(0.349, 0.866), resolution=(1080, 2400))):
                touch(Template(r"tpl1742267726571.png", record_pos=(0.349, 0.866), resolution=(1080, 2400)))
                break

    @staticmethod
    def quick_finish_timeline_guide():
        while True:#持续观看剧情，直到出现取名弹框
            touch((0.82,0.07))#一直点击跳过按钮的位置
            if exists(Template(r"tpl1742267528865.png", record_pos=(0.004, -0.299), resolution=(1080, 2400))):
                touch(Template(r"tpl1742267544544.png", record_pos=(-0.009, 0.027), resolution=(1080, 2400)))
                break
        while True:#重新判断，否则上一段判断的太多了执行太久
            touch((0.82,0.07))#一直点击跳过按钮的位置
            if exists(Template(r"tpl1742267601743.png", record_pos=(-0.231, -0.527), resolution=(1080, 2400)))  :#等待娜娜出现
                snapshot(msg="检查娜娜出场界面显示")
                break
        while True:#重新判断，否则上一段判断的太多了执行太久
            touch((0.82,0.07))#一直点击跳过按钮的位置
            if exists(Template(r"tpl1742267690704.png", record_pos=(-0.389, -0.685), resolution=(1080, 2400)))  :#等待娜娜结婚界面
                snapshot(msg="检查娜娜结婚界面显示")
                break
        while True:#重新判断，否则上一段判断的太多了执行太久
            touch((0.82,0.07))#一直点击跳过按钮的位置
            if exists(Template(r"tpl1742301266972.png", record_pos=(0.386, 0.866), threshold=0.5,resolution=(1080, 2400))):
                touch((0.5,0.88))
                break
                
    @staticmethod
    def finish_main_guild():
        # logging.info("开始执行finish_main_guild")
        # sleep(2)
        # touch((0.37,0.53))#后宫入口
        # NANA = Template(r"tpl1741684797239.png", record_pos=(-0.21, -0.617),
        #                 resolution=(1260, 2720))
        # touch(wait(NANA))
        # assert_exists(Template(r"tpl1741684892414.png", record_pos=(0.034, -0.228),
        #                        resolution=(1260, 2720)),
        #               "娜娜Spine展示正常")
        # for _ in range(6):  # 随便点一个地方,点7次，完成该界面的引导
        #     touch(casual)
        #     sleep(0.5)
        # sleep(1)
        public_using.touch_back()
        sleep(1)
        touch((0.8,0.89))#随机约会按钮，改成坐标
        sleep(5)
        NANA_Spine = Template(r"tpl1742269032909.png", record_pos=(-0.003, -0.478), resolution=(1080, 2400))
        wait(NANA_Spine,timeout=100)
        touch(casual)
        snapshot(msg="检查约会界面展示是否正常.")
        sleep(1.5)
        touch(casual)
        touch(casual)
        touch(casual)
        sleep(1.5)
        public_using.touch_back()
        sleep(3)
        try:
            touch((0.25, 0.8))
            sleep(1)
            touch(casual)
        except AssertionError as e:
            print("第一个任务未完成")
        touch(wait(Template(r"tpl1741685701535.png", record_pos=(0.204, 0.676),
                            resolution=(1260, 2720))))
        page2_ensure_post = wait(
            Template(r"tpl1741685701535.png", record_pos=(0.204, 0.676),
                     resolution=(1260, 2720)))
        for _ in range(6):
            touch(page2_ensure_post)
        sleep(1)
        public_using.close_face_window()
        logging.info("结束执行finish_main_guild")

if __name__ == "__main__":
    os.chdir(r"H:\Uiauto_demo\data")
    MainStep.quick_finish_timeline_guide()
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)














