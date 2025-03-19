from airtest.core.api import *

device_screen = {
    "23E0224711011260": (2720, 1260),
    "emulator-5554": (1920, 1080)
}

casual = (0.5, 0.08)

blank_icon = Template(r"blank_title_icon.png", record_pos=(0.228, 0.15), resolution=(1260, 2720),
                      threshold=0.8, rgb=True)

star = Template(r"H:\Uiauto_demo\scripts\drag_drop\tpl1741614611952.png", record_pos=(-0.357, -0.1),
                resolution=(2720, 1260))
