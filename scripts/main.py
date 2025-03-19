# -*- encoding=utf8 -*-
__author__ = "Ashe Li"
__title__ = "主脚本"
__desc__ = "新手引导-》主线引导-》玩家信息   -》商城-》政务大厅"

import logging
import os
import sys

sys.path.append(r"H:\Uiauto_demo")
from airtest.core.api import *

from lib.general_operation import GeneralOperation
from airtest.report.report import simple_report
from airtest.core.android.adb import *
from scripts.main_step import main_step
from scripts.guide_task import guide_task
from scripts.player_info import player_info_smoke
from scripts.office import office_smoke
GeneralOperation.set_logging_config()  # 设置log级别为info

def start_smoke_test():
    # start_app("com.nata.refantasia.android")
    # main_step.MainStep.test_timeline_guild()
    # main_step.MainStep.quick_finish_timeline_guide()
    # main_step.MainStep.finish_main_guild()
    guide_task.start_guide_task_smoke_test()
    player_info_smoke.TestPlayerInfo()
    office_smoke.HandleOffice()


if __name__ == "__main__":
    # 设置脚本运行路径为图片所在路径，避免出现路径问题导致找不到图片
    os.chdir(r"H:\Uiauto_demo\data")
    logging.info(f"打印当前运行路径{os.getcwd()}")
    try:
        start_smoke_test()
    finally:
        log_dir = GeneralOperation.get_device_and_logdir()
        simple_report(__file__, logpath=log_dir, logfile="log.txt",
                      output=os.path.join(log_dir, f"somke_test_report.html"))
