# -*- encoding=utf8 -*-
__author__ = "ASUS"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/emulator-5554?", ])

# script content
print("start...")


def test_battle_guide():
    casual_pos = (0.5, 0.1)
    touch(wait(Template(r"tpl1741758553225.png", record_pos=(0.087, 0.885), resolution=(1260, 2720))))
    click_skip_dialog()
    touch(wait(Template(r"tpl1741758629131.png", record_pos=(0.337, 0.556), resolution=(1260, 2720))))
    touch(wait(Template(r"tpl1741758655783.png", record_pos=(0.179, 0.035), resolution=(1260, 2720))))
    wait(Template(r"tpl1741758674650.png", record_pos=(-0.331, -0.449), resolution=(1260, 2720)))
    for _ in range(2):
        touch(casual_pos)
        sleep(0.5)
    touch(wait(Template(r"tpl1741758807282.png", record_pos=(0.408, 0.909), resolution=(1260, 2720))))
    assert_exists(Template(r"tpl1741758854048.png", record_pos=(0.006, 0.015), resolution=(1260, 2720)),
                  "检查背景图显示是否正常")
    sleep(0.5)
    while True:  # 战斗会自动攻击，等待战斗胜利
        wait(Template(r"tpl1741758903634.png", record_pos=(0.019, -0.156), resolution=(1260, 2720)))
        break
    touch(Template(r"tpl1741758941990.png", record_pos=(0.187, 0.44), resolution=(1260, 2720)))
    click_skip_dialog()  # 尝试跳过
    if exists(Template(r"tpl1741759001962.png", record_pos=(0.365, -0.911), resolution=(1260, 2720))):
        # 说明没有跳过，存在剧情分支
        touch(Template(r"tpl1741759030823.png", record_pos=(0.01, -0.087), resolution=(1260, 2720)))
    # 如果剧情分支没有选择成功，则再点击一次
    if exists(Template(r"tpl1741759030823.png", record_pos=(0.01, -0.087), resolution=(1260, 2720))):
        touch(Template(r"tpl1741759030823.png", record_pos=(0.01, -0.087), resolution=(1260, 2720)))
    else:
        click_skip_dialog()  # 继续跳过
    while True:
        sleep(2)  # 战斗会自动攻击，每2秒检查一次，战斗是否胜利
        wait(Template(r"tpl1741758903634.png", record_pos=(0.019, -0.156), resolution=(1260, 2720)))
        break
    touch(wait(Template(r"tpl1741759272568.png", record_pos=(0.195, 0.448), resolution=(1260, 2720))), duration=0.5)


def click_skip_dialog():
    touch(wait(Template(r"tpl1741758583724.png", record_pos=(0.368, -0.905), resolution=(1260, 2720))), duration=0.5)


if __name__ == "__main__":
    test_battle_guide()

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
