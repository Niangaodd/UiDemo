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
# auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/192.168.110.175:55555?touch_method=MAXTOUCH&",])
print("start...")

class MainStep:
    @staticmethod
    def finish_main_guild():
        logging.info("开始执行finish_main_guild")
        touch(wait(Template(r"H:\Uiauto_demo\scripts\main_step\tpl1741684779769.png", record_pos=(-0.134, 0.083),
                            resolution=(1260, 2720))))
        NANA = Template(r"H:\Uiauto_demo\scripts\main_step\tpl1741684797239.png", record_pos=(-0.21, -0.617),
                        resolution=(1260, 2720))
        touch(wait(NANA))
        assert_exists(Template(r"H:\Uiauto_demo\scripts\main_step\tpl1741684892414.png", record_pos=(0.034, -0.228),
                               resolution=(1260, 2720)),
                      "娜娜Spine展示正常")
        for _ in range(6):  # 随便点一个地方,点7次，完成该界面的引导
            touch(casual)
            sleep(0.5)
        sleep(1)
        public_using.touch_back()
        touch(wait(Template(r"H:\Uiauto_demo\scripts\main_step\tpl1741685057297.png", record_pos=(0.322, 0.88),
                            resolution=(1260, 2720))))
        NANA_Spine = Template(r"H:\Uiauto_demo\scripts\main_step\tpl1741685077055.png", record_pos=(0.015, 0.047),
                              resolution=(1260, 2720))
        wait(NANA_Spine)
        assert_exists(NANA_Spine, "检查约会界面展示是否正常")
        sleep(0.5)
        touch(casual)
        public_using.touch_back()
        sleep(3)
        try:
            touch((0.25, 0.8))
            sleep(1)
            touch(casual)
        except AssertionError as e:
            print("第一个任务未完成")
        touch(wait(Template(r"H:\Uiauto_demo\scripts\main_step\tpl1741685701535.png", record_pos=(0.204, 0.676),
                            resolution=(1260, 2720))))
        page2_ensure_post = wait(
            Template(r"H:\Uiauto_demo\scripts\main_step\tpl1741685701535.png", record_pos=(0.204, 0.676),
                     resolution=(1260, 2720)))
        for _ in range(6):
            touch(page2_ensure_post)
        sleep(1)
        public_using.close_face_window()
        logging.info("结束执行finish_main_guild")

if __name__ == "__main__":
    MainStep.finish_main_guild()

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)



