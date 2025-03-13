# -*- encoding=utf8 -*-
__author__ = "Ashe Li"
__title__ = "完成第一步强制引导"
__desc__ = "从后宫引导-》领取第一个引导任务的奖励"

import sys

sys.path.append(r"H:\Uiauto_demo")
from airtest.core.api import *
from airtest.cli.parser import cli_setup

# if not cli_setup():
#     auto_setup(__file__, logdir=True, devices=["Android:///",])


# script content
print("start...")


def finish_main_guild():
    casual = (0.5, 0.08)
    touch(casual)
    touch(wait(Template(r"H:\Uiauto_demo\scripts\main_step\tpl1741684779769.png", record_pos=(-0.134, 0.083),
                        resolution=(1260, 2720))))
    NANA = Template(r"H:\Uiauto_demo\scripts\main_step\tpl1741684797239.png", record_pos=(-0.21, -0.617),
                    resolution=(1260, 2720))
    NANA_pos = wait(NANA)
    touch(NANA_pos)
    assert_exists(Template(r"H:\Uiauto_demo\scripts\main_step\tpl1741684892414.png", record_pos=(0.034, -0.228),
                           resolution=(1260, 2720)),
                  "娜娜Spine展示正常")
    for _ in range(7):  # 随便点一个地方,点7次，完成该界面的引导
        touch(casual)
        sleep(1)
    sleep(1)
    touch(wait(Template(r"H:\Uiauto_demo\scripts\main_step\tpl1741685000757.png", record_pos=(-0.436, -0.865),resolution=(1260, 2720))))
    touch(wait(Template(r"H:\Uiauto_demo\scripts\main_step\tpl1741685057297.png", record_pos=(0.322, 0.88),
                        resolution=(1260, 2720))))
    NANA_Spine = Template(r"H:\Uiauto_demo\scripts\main_step\tpl1741685077055.png", record_pos=(0.015, 0.047),
                          resolution=(1260, 2720))
    wait(NANA_Spine)
    assert_exists(NANA_Spine, "检查约会界面展示是否正常")
    touch(casual)
    touch(wait(Template(r"H:\Uiauto_demo\scripts\main_step\tpl1741685000757.png", record_pos=(-0.436, -0.865),resolution=(1260, 2720))))
    sleep(3)
    try:
        touch((0.25, 0.8))
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
    if exists(Template(r"H:\Uiauto_demo\scripts\main_step\tpl1741695450607.png", record_pos=(-0.011, -0.27),
                       resolution=(1260, 2720))):
        touch(casual)
    else:
        for _ in range(5):  # 如果存在拍脸弹窗,点击关闭，检查5次，可能有多个弹窗
            if exists(Template(r"H:\Uiauto_demo\scripts\main_step\tpl1741685805003.png", record_pos=(0.447, -0.797),
                               resolution=(1260, 2720))):
                touch(Template(r"H:\Uiauto_demo\scripts\main_step\tpl1741685813499.png", record_pos=(0.441, -0.792),
                               resolution=(1260, 2720)))
                sleep(0.5)


if __name__ == "__main__":
    finish_main_guild()

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
