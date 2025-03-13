import logging
import time
from airtest.core.helper import set_logdir
from airtest.core.settings import Settings as ST
import os


class GeneralOperation:

    @staticmethod
    def set_logPath(file_path):
        # 构造日志文件名称为，脚本名称加_log.txt
        ST.LOG_FILE = os.path.splitext(os.path.basename(file_path))[0] + '_log.txt'
        set_logdir(r'H:\Uiauto_demo\logs')
        print("设置日志地址了")

    @staticmethod
    def build_record_path(file_path):
        """
        处理跨平台时，使用当前时间戳作为文件名，构造mp4的完整路径
        :param file_path:传入__file__
        :return: mp4的完整路径
        """
        script_dir = os.path.dirname(file_path)#获取脚本当前所在目录
        name = str(int(time.time()))#使用时间戳作为录屏文件的名字
        record_path = os.path.join(script_dir,name) + '.mp4'
        print(record_path)
        return record_path

    @staticmethod
    def pos_absolute_to_relative(pos,width, height):
        """横屏模式，绝对坐标转换相对坐标"""
        # 横屏时分辨率应表示为 (长边, 短边)
        x1 = round(pos[0] / width,3)#保留三位小数
        y1 = round(pos[1] / height,3)
        return (x1,y1)

    @staticmethod
    def pos_relative_to_absolute(pos,width, height):
        """横屏模式，相对坐标转换绝对坐标
        :param pos:传入元组（x,Y）
        :return: (x,y)
        """
        # 横屏时分辨率应表示为 (长边, 短边)
        x1 = round(pos[0] * width) #四舍五入
        y1 = round(pos[1] * width)
        return (x1,y1)

    @staticmethod
    def new_logging():
        logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(message)s")

    @staticmethod
    def get_device_and_logdir():
        device_id = os.getenv("DEVICE_ID")
        log_dir = os.getenv("LOG_DIR")
        logging.info(f"设备id是{device_id}")
        logging.info(f"日志dir是{log_dir}")
        return device_id,log_dir

if __name__ ==  "__main__":
    x = GeneralOperation.pos_absolute_to_relative((389,359),2720,1260)
    Y = GeneralOperation.pos_relative_to_absolute((0.143, 0.285),2720,1260)

    print(x)
    print(Y)

