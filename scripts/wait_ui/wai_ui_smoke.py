# -*- encoding=utf8 -*-
__author__ = "ASUS"
import sys
sys.path.append(r"H:\Uiauto_demo")
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from scprits.home_page import home_page

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/23E0224711011260?touch_method=MAXTOUCH&",])
    
def click_item():
    touch(Template(r"tpl1741681097039.png", record_pos=(-0.268, 0.1), resolution=(2720, 1260)))
    boom = Template(r"H:\Uiauto_demo\scprits\wait_ui\boom.png",resolution=(2720,1260))
    chicken = Template(r"H:\Uiauto_demo\scprits\wait_ui\chicken.png",resolution=(2720,1260))
    shark = Template(r"H:\Uiauto_demo\scprits\wait_ui\shark.png",resolution=(2720,1260))
    targets = [boom,chicken,shark]
    result = []
    while True:
        for i in targets:
            sleep(1.5)
            if exists(i):
                snapshot(msg="检查出现的图案")
                touch(i)
                result.append(i)
        if len(set(result)) == 3:
            assert_equal("出现并点击了3种图案", "出现并点击了3种图案", "检查3种图案是否都能出现并点击")
            print("三个元素都出现过")
            break
    home_page.click_back()

click_item()
# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)