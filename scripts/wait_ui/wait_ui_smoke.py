# -*- encoding=utf8 -*-
__author__ = "ASUS"
import sys
sys.path.append(r"H:\Uiauto_demo")
from airtest.core.api import *
from scripts.home_page import home_page

    
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


if __name__ == "__main__":
    click_item()