# -*- encoding=utf8 -*-
__author__ = "ASUS"

import sys

sys.path.append(r"H:\Uiauto_demo")
from config import blank_icon
from airtest.core.api import *
from lib.general_operation import *
GeneralOperation.new_logging()
# script content
print("start...")


class TestDiamondShop:
    def __init__(self):
        self.enter_shop()
        self.test_daily_shop()
        self.test_level_shop()
        self.test_vip_shop()

    def enter_shop(self):
        touch(wait(Template(r"../../data/tpl1741754731656.png", record_pos=(0.413, 0.91), resolution=(1080, 2400))))
        sleep(3)  # 等待商城次首次加载
        assert_exists(Template(r"../../data/tpl1741754782890.png", record_pos=(-0.002, -0.547), resolution=(1080, 2400)),
                      "检查商城页签显示是否正常")
        self.test_exists_blank_icon()

    def test_level_shop(self):
        touch(Template(r"../../data/tpl1741757487756.png", target_pos=8, record_pos=(0.118, -0.606), resolution=(1080, 2400)))
        self.test_exists_blank_icon()

    def test_daily_shop(self):
        touch(Template(r"../../data/tpl1741757250741.png", record_pos=(-0.126, -0.576), resolution=(1080, 2400)))
        wait(Template(r"../../data/tpl1741757272123.png", record_pos=(-0.353, 0.637), resolution=(1080, 2400)))
        self.test_exists_blank_icon()
        sleep(1)
        # 购买一个金币，查看是否扣除魔晶
        touch(Template(r"../../data/tpl1741757315407.png", record_pos=(0.341, -0.263), resolution=(1080, 2400)), duration=0.5)
        try:
            assert_not_exists(
                Template(r"../../data/tpl1741757366839.png", threshold=0.95, record_pos=(0.344, -0.967), resolution=(1080, 2400)),
                "检查购买道具后，魔晶是否扣除")
        except AssertionError as e:
            logging.info(f"购买道具后，魔晶数量未改变{e}")

    def test_vip_shop(self):
        touch(Template(r"../../data/tpl1741757744428.png", record_pos=(0.35, -0.575), resolution=(1080, 2400)))
        assert_exists(Template(r"../../data/tpl1741754847724.png", record_pos=(-0.002, 0.056), resolution=(1080, 2400)),
                      "检查VIP商城的商品列表展示")
        self.test_exists_blank_icon()
        sleep(1)
        try:
            touch(Template(r"../../data/tpl1741754924281.png", target_pos=9, record_pos=(-0.257, -0.308), resolution=(1080, 2400)))
            sleep(1)
            touch(Template(r"../../data/tpl1741754945202.png", target_pos=9, record_pos=(0.218, -0.297), resolution=(1080, 2400)))
            sleep(1)
            assert_exists(Template(r"../../data/tpl1741755434182.png", record_pos=(0.071, -0.275), resolution=(1080, 2400)),
                          "检查领取免费奖励后，按钮状态是否改变")
        except AssertionError as e:
            logging.info(f"领取vip商城的免费商品后，按钮没有变成售罄")

    def test_exists_blank_icon(self):
        try:
            assert_not_exists(blank_icon, "检查是否存在空白图")
        except AssertionError as e:
            logging.info(f"存在空白图{e}")


if __name__ =="__main__":
    exe = TestDiamondShop()
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)



