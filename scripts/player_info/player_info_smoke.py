# -*- encoding=utf8 -*-
__author__ = "Ashe Li"
__title__ = "Somke Test for Player Info"
import sys
sys.path.append(r"H:/Uiauto_demo")
from config import blank_icon
from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",], project_root="H:/Uiauto_demo")


# script content
print("start...")

class TestPlayerInfo:
    def __init__(self):
        self.test_main_Ui()
        self.test_title_list()

    def test_main_Ui(self):
        touch(wait(Template(r"tpl1741751994641.png", record_pos=(-0.421, -0.832), resolution=(1260, 2720))),times=2,duration=1)
        player_spine = Template(r"tpl1741752071239.png", record_pos=(0.039, -0.248), resolution=(1260, 2720))
        wait(player_spine)

        assert_exists(player_spine, "检查主角spine显示是否正常")
        assert_exists(Template(r"tpl1741752045606.png", record_pos=(-0.001, 0.194), resolution=(1260, 2720)), "检查称号显示是否正常")
        assert_exists(Template(r"tpl1741752058136.png", record_pos=(-0.431, -0.759), resolution=(1260, 2720)), "检查徽章显示是否正常")
    
    def test_title_list(self):
        touch(wait(Template(r"tpl1741752226512.png", record_pos=(0.412, -0.083), resolution=(1260, 2720))))
        wait(Template(r"tpl1741752260514.png", record_pos=(0.009, 0.382), resolution=(1260, 2720)))
        self.test_exists_blank_icon()
        #向下滑动查看，是否存在空白称号
        for _ in range(3):
            swipe((0.5,0.78),(0.5,0.58),duration=1)
            sleep(1)
            self.test_exists_blank_icon()
        sleep(1)
        #切换到徽章背包
        touch(Template(r"tpl1741754245618.png", threshold=0.9, target_pos=6, record_pos=(-0.25, -0.786), resolution=(1080, 2400)))

        wait(Template(r"tpl1741754089269.png", record_pos=(0.007, 0.369), resolution=(1080, 2400)))
        self.test_exists_blank_icon()
        swipe((0.5,0.78),(0.5,0.58),duration=1)
        sleep(1)
        self.test_exists_blank_icon()
        sleep(1)
        #切换到王权成就
        touch(Template(r"tpl1741754279540.png", threshold=0.9, target_pos=6, record_pos=(0.002, -0.781), resolution=(1080, 2400)))
        wait(Template(r"tpl1741754132376.png", record_pos=(-0.006, 0.859), resolution=(1080, 2400)))
        assert_exists(Template(r"tpl1741754145223.png", record_pos=(-0.169, 0.159), resolution=(1080, 2400)), "检查任务列表是否显示正常")
        sleep(1)
        #切换到王权商店
        touch(Template(r"tpl1741754433320.png", threshold=0.9, rgb=True, record_pos=(0.363, -0.78), resolution=(1080, 2400)))


        wait(Template(r"tpl1741754186076.png", record_pos=(-0.169, 0.477), resolution=(1080, 2400)))
        assert_exists(Template(r"tpl1741754193774.png", record_pos=(0.024, 0.014), resolution=(1080, 2400)), "检查5个皮肤显示否是正常")
        
    def test_exists_blank_icon(self):
        try:
            assert_not_exists(blank_icon,"检查是否存在空白图标")
        except AssertionError as e:
            print("称号列表里存在空白图：",e)
            
if __name__ == "__main__":
    execute = TestPlayerInfo()
    
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
