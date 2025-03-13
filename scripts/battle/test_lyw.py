# -*- encoding=utf8 -*-
__author__ = "ASUS"
import sys
sys.path.append(r"H:\Uiauto_demo")
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from config import blank_icon
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/192.168.110.175:55555?touch_method=MAXTOUCH&",])


# script content
print("start...")

assert_exists(blank_icon,"存在空白图")
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)