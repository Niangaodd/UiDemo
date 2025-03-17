pem 打开一个新窗口，使用雷电模拟器执行guide_task的UI自动化脚本

start "test->leidian->guide_task" cmd /k "set DEVICE_ID=emulator-5554&&set LOG_DIR=H:\Uiauto_demo\scripts\guide_task\log\emulator-5554&&airtest run H:\Uiauto_demo\scripts\guide_task\guide_task.py"
echo 已启动测试任务

pem 打开一个新窗口，使用华为mate60pro执行guide_task的UI自动化脚本

start "test->HWmate60pro->guide_task" cmd /k "set DEVICE_ID=23E0224711011260&&set LOG_DIR=H:\Uiauto_demo\scripts\guide_task\log\23E0224711011260&&airtest run H:\Uiauto_demo\scripts\guide_task\guide_task.py"

echo 已启动测试任务
