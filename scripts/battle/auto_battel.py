# -*- encoding=utf8 -*-
__author__ = "Ashe Li"
__title__ = "重复战斗，自动战斗"
__desc__ = """1.进入关卡 2.点击攻击 3.判断是否存在剧情 4、循环点击剧情、判断是否存在空白图、是否存在Nokey，剧情关闭后braek 5、每个第5关是boss关，需要做一次判断 6、小兵关卡：判断背景图、判断小兵模型、判断敌人小兵模型、"""

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android:///", ])

# script content
print("start...")
current_chapter = 1
end_chapter = 10
battle_id = 1
option_1 = (0.48, 0.5)

def auto_battle(current_chapter, battle_id=1):
    casual_pos = (0.5, 0.1)

    #     touch(Template(r"tpl1741761353076.png", record_pos=(0.08, 0.88), resolution=(1080, 2400)))
    while True:
        auto_read_dialog()
        wait(Template(r"tpl1741761358634.png", record_pos=(0.336, 0.557), resolution=(1080, 2400)))
        snapshot(filename=rf"关卡列表第{current_chapter}章截图.png", msg=f"关卡列表第{current_chapter}章截图")
        touch(Template(r"tpl1741761358634.png", record_pos=(0.336, 0.557), resolution=(1080, 2400)),duration=0.5)
        sleep(1)
        if exists(Template(r"tpl1741774376650.png", threshold=0.6, rgb=True, record_pos=(0.172, 0.033), resolution=(1260, 2720))):
            touch(Template(r"tpl1741774376650.png", threshold=0.6, rgb=True, record_pos=(0.172, 0.033), resolution=(1260, 2720)))
        auto_read_dialog()
        # 剧情看完之后，检查对局状态，先判断当前是普通关还是boss关
        if battle_id != 6:  # 普通关卡
            sleep(1.5)
            snapshot(filename=f"关卡第{current_chapter}章第{battle_id}关截图.png",
                     msg=f"关卡第{current_chapter}章第{battle_id}关截图")
            while True:  # 战斗会自动攻击，等待战斗胜利
                try:
                    if exists(Template(r"tpl1741758903634.png", threshold=0.7, record_pos=(0.019, -0.156),
                                  resolution=(1260, 2720))):
                        touch(Template(r"1741774789648.png", threshold=0.8, record_pos=(0.22, -0.62), resolution=(1260, 2720)))
                        break
                except Exception as e:
                    print("循环查找战斗胜利出现异常：",e)
            battle_id += 1
        else:
            snapshot(filename=rf"关卡第{current_chapter}章BOSS关截图.png",
                     msg=f"关卡第{current_chapter}章BOSS关截图.png")
            while True:  # 战斗会自动攻击，等待战斗胜利
                try:
                    touch(Template(r"tpl1741776164016.png", record_pos=(0.406, 0.913), resolution=(1260, 2720)))
                    if exists(Template(r"tpl1741758903634.png", threshold=0.7, record_pos=(0.019, -0.156),
                                  resolution=(1260, 2720))):
                        touch(Template(r"1741774789648.png", threshold=0.8, record_pos=(0.22, -0.62), resolution=(1260, 2720)))
                        break
                    else:
                        touch(Template(r"tpl1741776164016.png", record_pos=(0.406, 0.913), resolution=(1260, 2720)))
                except Exception as e:
                    print("循环查找战斗胜利出现异常：",e)
            battle_id = 0
            current_chapter += 1
            if exists(Template(r"tpl1741775116803.png", record_pos=(-0.006, -0.894), resolution=(1260, 2720))):
                touch(casual_pos)

def click_skip_dialog():
    touch(wait(Template(r"tpl1741758583724.png", record_pos=(0.368, -0.905), resolution=(1260, 2720))), duration=0.5)


def auto_read_dialog():
    if exists(Template(r"tpl1741759001962.png", record_pos=(0.365, -0.911), resolution=(1260, 2720))):
        # 无限循环观看剧情，直到消失
        while True:
            # 先判断是否存在剧情
            if exists(Template(r"tpl1741761647125.png", record_pos=(0.362, -0.937), resolution=(1080, 2400))):
                touch(option_1)
            else:
                break

if __name__ == "__main__":
    auto_battle(3, 1)
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)

# from airtest.aircv.cal_confidence import *
# img1 = cv2.resize(cv2.imread(r"C:\Users\ASUS\Desktop\main_ui.jpg"),(1080,1920))
# snapshot(filename=r"C:\Users\ASUS\Desktop\main_ui2.jpg",msg="请填写测试点.")
# sleep(10)
# img2 = cv2.resize(cv2.imread(r"C:\Users\ASUS\Desktop\main_ui2.jpg"),(1080,1920))
# confidence = cal_ccoeff_confidence(img1,img2)
# print("输出可信度",confidence)



