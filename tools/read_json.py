import json
import os

from conftest import BASE_PATH
from tools.get_log import GetLog

log = GetLog.get_logger()

# 读取json文件的函数
log.info("调用读取json文件的函数")


def read_json(filename):
    """
    :param filename: 文件名称
    :return:
    """
    # 读取文件路径
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename
    log.info("读取文件路径为：" + str(file_path))
    # 读取文件
    log.info("读取文件")
    with open(file_path, "r", encoding='utf-8') as ef:
        # 以列表的形式返回读取文件
        log.info("返回读取文件")
        return list(json.load(ef).values())
        # print(ssl)


if __name__ == '__main__':
    read_json("login.json")
