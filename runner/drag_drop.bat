@echo off

rem 启动雷电模拟器测试（新窗口）
rem start "TEST leidian" cmd /k "set DEVICE_ID=emulator-5554&&set LOG_DIR=H:\Uiauto_demo\scprits\drag_drop\log\emulator-5554&&airtest run H:\Uiauto_demo\scprits\basic\drag_drop_smoke.py"

rem 启动华为Mate60 Pro测试（新窗口）
start "TEST mate60pro" cmd /k "set DEVICE_ID=23E0224711011260&&set LOG_DIR=H:\Uiauto_demo\scprits\drag_drop\log\HW_mate60_pro&&airtest run H:\Uiauto_demo\scprits\basic\drag_drop_smoke.py"

echo 已启动所有测试任务，请查看新窗口中的运行进度

pause

