# -*- encoding=utf8 -*-
__author__ = "Ashe Li"
__title__ = '移动星星，测试玩法'
__desc__ = '''进入星星界面-》判断星星是否存在-》移动星星-》判断结果-》返回功能列表'''


import sys
import logging
import os
import time

sys.path.append(r"H:\Uiauto_demo")
from lib.general_operation import *
from scripts.home_page import home_page
from airtest.core.api import *
from lib.general_operation import GeneralOperation
from airtest.report.report import simple_report
from airtest.cli.parser import cli_setup
from airtest.core.android import Android
import config

GeneralOperation.new_logging()

# if not cli_setup():
#     auto_setup(__file__, 
#                logdir=True,
#                devices=["Android://127.0.0.1:5037/emulator-5554","Android://127.0.0.1:5037/23E0224711011260"])
# 从环境变量获取设备ID和日志目录
device_id,log_dir = GeneralOperation.get_device_and_logdir()
# 初始化时指定独立目录
auto_setup(__file__, logdir=log_dir, devices=[f"Android://127.0.0.1:5037/{device_id}"])


def enter_drap_drop():
    """判断是否进入玩法界面，返回星星列表stars_pos包含所有星星的坐标"""
    touch(Template(r"tpl1741660551575.png", record_pos=(-0.263, -0.076), resolution=(2720, 1260)))
    sleep(1)
    star = Template(r"tpl1741614611952.png", record_pos=(-0.357, -0.1), resolution=(2720, 1260))
    star_is_exists = exists(star)
    if star_is_exists:
        star_list = find_all(star)
    # logging.info(f"star_list:{star_list}")
    stars_pos = []
    for i in star_list:
        star_pos = i["result"]
        stars_pos.append(star_pos)
    # logging.info(f"stars_pos:{stars_pos}")
    assert_equal(len(stars_pos), 5, "预期存在5颗星星")
    assert_exists(Template(r"tpl1741661033694.png", record_pos=(-0.251, -0.182), resolution=(2720, 1260)),
                  "预期初始分数为0")
    return stars_pos


def move_star(stars_pos):
    shell_pos = (0.52, 0.7)
    # 移动星星
    for star in stars_pos:
        swipe(star, shell_pos)
    sleep(2)
    # 移动后判断星星是否消失
    assert_not_exists(Template(r"tpl1741614611952.png", record_pos=(-0.357, -0.1), resolution=(2720, 1260)),
                      "移动星星后，星星消失在界面上")
    assert_exists(Template(r"tpl1741661098382.png", record_pos=(-0.235, -0.183), resolution=(2720, 1260)),
                  "预期移动结束后分数为100")
    home_page.click_back()

    
if __name__ == "__main__":
    # home_page.enter_homepage()
    stars_pos = enter_drap_drop()
    logging.info(f"stars_pos:{stars_pos}")
    move_star(stars_pos)
