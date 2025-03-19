import os

script_path = os.path.abspath(__file__)#获取脚本所在的绝对路径，避免运行环境的问题
script_dir = os.path.dirname(script_path)


print(__file__)
print(script_path)
print(script_dir)

dir_1 = r"H:\Uiauto_demo\temporary.py"
result = os.path.isabs(dir_1)
print(result)
print(os.getcwd())