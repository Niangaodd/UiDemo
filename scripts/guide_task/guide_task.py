# -*- encoding=utf8 -*-
__author__ = "Ashe Li"
__title__ = "完成引导任务step2-step10"
__desc__ = "从第二个引导任务完成至第十个引导任务"

import sys

sys.path.append(r"H:\Uiauto_demo")
import logging
from airtest.core.api import *
from config import casual
from lib import public_using
from lib.general_operation import GeneralOperation
GeneralOperation.set_logging_config()
# script content
print("start...")


def taskui_is_open():
    """先判断任务面板是否打开，如果打开，则处理任务点击跳转/领奖，如果未打开，点击则任务入口试图打开任务面板"""
    if exists(Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741691933991.png", threshold=0.8,
                       record_pos=(0.002, -0.234), resolution=(1260, 2720))):
        handle_task_result()
    else:
        if exists(Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741691987650.png", record_pos=(-0.337, 0.64),
                           resolution=(1260, 2720))):
            touch((0.25, 0.8))
            handle_task_result()  # 根据任务状态做下一步操作
        else:
            touch((0.25, 0.8))
            congratulae_is_open()

def handle_task_result():
    """打开引导任务面板后，根据领奖状态判断点击前往/领奖"""
    wait(Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741693224105.png", record_pos=(0.003, -0.229),
                  resolution=(1260, 2720)))
    jmup_icon = Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741692128849.png", record_pos=(-0.001, 0.223),
                         resolution=(1260, 2720))
    if exists(jmup_icon):
        touch(wait(Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741687981056.png", record_pos=(0.004, 0.223),
                            resolution=(1260, 2720))))
    else:
        assert_exists(Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741701709861.png", record_pos=(0.003, 0.21),
                               resolution=(1080, 2400)),
                      "检查是否为领奖状态")
        sleep(1)
        touch(wait(Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741701709861.png", record_pos=(0.003, 0.21),
                            resolution=(1080, 2400))), duration=0.5)
        congratulae_is_open()
        touch(casual)  # 关闭任务面板


def congratulae_is_open():
    """判断恭喜获得界面是否正常展示"""
    sleep(1)
    assert_exists(Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741691540115.png", record_pos=(0.012, -0.225),
                           resolution=(1260, 2720)),
                  "检查是否弹出恭喜获得界面")
    touch(casual)


def task_process_2to4():
    logging.info("开始执行task_process_2to4")# 2-》10
    taskui_is_open()
    collect_pos = wait(Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741688223745.png", record_pos=(0.013, 0.684),
                                resolution=(1260, 2720)))
    snapshot(msg="跳转后征收，截图")
    touch(collect_pos)
    touch(wait(Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741690238110.png", record_pos=(0.359, -0.912),
                        resolution=(1260, 2720))))
    wait(Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741691084886.png", record_pos=(-0.323, -0.082),
                  resolution=(1260, 2720)))
    for _ in range(3):
        sleep(1)
        touch(casual)

    gold_pos = wait(
        Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741690749117.png", target_pos=8, record_pos=(0.2, -0.326),
                 resolution=(1260, 2720)))
    food_pos = wait(
        Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741690961626.png", target_pos=8, record_pos=(0.217, 0.038),
                 resolution=(1260, 2720)))

    soldier_pos = wait(
        Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741690940986.png", target_pos=8, record_pos=(0.223, 0.339),
                 resolution=(1260, 2720)))
    for _ in range(3):
        touch(gold_pos)
        sleep(0.5)
        touch(food_pos)
        sleep(0.5)
        touch(soldier_pos)
        sleep(0.5)
    touch((0.53, 0.17))
    sleep(1)
    #这一步要改，老点不到政务
    touch((0.20,0.47))
    touch(wait(Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741690238110.png", record_pos=(0.359, -0.912),
                        resolution=(1260, 2720))), duration=1)
    wait(Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741691084886.png", record_pos=(-0.323, -0.082),
                  resolution=(1260, 2720)))
    touch(casual)
    for _ in range(3):
        touch((0.44, 0.63))
        sleep(0.7)
    touch((0.53, 0.17))
    sleep(0.7)
    public_using.touch_back()
    sleep(0.7)
    handle_task_result()
    taskui_is_open()
    taskui_is_open()
    logging.info("结束执行task_process_2to4")

def task_process_5():
    logging.info("开始执行task_process_5")
    taskui_is_open()
    touch(wait(Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741692378201.png", record_pos=(-0.336, -0.466),
                        resolution=(1260, 2720))))
    for _ in range(6):
        touch(casual)
        sleep(0.8)
    sleep(1)
    up_btn_pos = wait(Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741692518445.png", record_pos=(0.399, 0.455),
                               resolution=(1260, 2720)))
    sleep(1)
    touch(up_btn_pos, duration=1)
    sleep(2)
    assert_exists(Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741692596053.png", record_pos=(0.009, 0.575),
                           resolution=(1260, 2720)),
                  "检查布莱克是否升级成功")
    # 把布莱克升级到20级，还需18次升级
    up_btn_pos = wait(Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741692518445.png", record_pos=(0.399, 0.455),
                               resolution=(1260, 2720)))
    for _ in range(21):
        sleep(0.5)
        # 如果提前升到23级了则提前结束
        if exists(
                Template(r"H:\Uiauto_demo\scripts\guide_task\tpl1741693043063.png", threshold=0.95,
                         record_pos=(-0.006, 0.575), resolution=(1260, 2720))):
            break
        touch(up_btn_pos)
    public_using.touch_back()
    public_using.touch_back()
    handle_task_result()
    logging.info("结束执行task_process_5")

def start_guide_task_smoke_test():
    task_process_2to4()
    task_process_5()


if __name__ == "__main__":
    #     task_process_2to4()
    task_process_5()
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
