# -*- encoding=utf8 -*-
__author__ = "Ashe Li"
__title__ = '设置玩家基础信息'
__desc__ = '''
1.进入玩家信息界面
2.输入名称
3.返回功能列表
'''

import sys
sys.path.append(r"H:\Uiauto_demo")
import config
from airtest.core.api import *
from scripts.home_page import home_page
from airtest.cli.parser import cli_setup


if not cli_setup():
    auto_setup(__file__, 
               logdir=True,
               devices=["Android://127.0.0.1:5037/emulator-5554","Android://127.0.0.1:5037/23E0224711011260"])

class TestBaisc():
    def __init__(self):
        self.lienEdit = Template(r"tpl1741679904328.png", record_pos=(-0.065, 0.037), resolution=(2720, 1260))

    def enter_basic(self):
        touch(Template(r"tpl1741679361185.png", record_pos=(-0.258, -0.135), resolution=(2720, 1260)))
        assert_exists(config.star, "检查星星是否存在")
        assert_exists(self.lienEdit, "检查输入框默认内容是否正确")
        
    def input_playerName(self):
        touch(self.lienEdit)
        text("OCTAGON")
        touch((500, 500))
        assert_exists(Template(r"tpl1741680561890.png", record_pos=(-0.063, 0.038), resolution=(2720, 1260)),"检查输入框输入后的状态")

        
if __name__ == "__main__":
    bs = TestBaisc()
    bs.enter_basic()
    bs.input_playerName()
    home_page.click_back()
    
   

