import os

import pytest

from tools.get_driver import GetDriver
from tools.read_json import read_json
from page.sale.login import PageLogin
from tools.get_log import GetLog

log = GetLog.get_logger()
import allure


@allure.epic("LILISHOP商城购物系统")
@allure.feature("登录模块")
class TestLogin:
    # 初始化
    log.info("初始化")

    def setup_class(self):
        # 初始化json数据
        pathdir = os.sep + "sale" + os.sep + "login.json"
        self.data_json = read_json(pathdir)
        # 初始化driver
        self.driver = GetDriver().get_driver(self.data_json[0])

    # 结束
    log.info("结束")

    def teardown_class(self):
        self.driver.quit()

    # 调用page层的综合调用方法
    log.info("调用page层的综合调用方法")


    @allure.title("登录方法")
    def test_login(self):
        PageLogin(self.driver).page_login(self.data_json[1], self.data_json[2])
        # 避免因为错误导致脚本异常中断
        try:
            # 判断是否登录成功
            log.info("断言成功")
            assert PageLogin(self.driver).page_get_word() == self.data_json[3]
        # 未成功，抛出异常
        except Exception as e:
            log.info("断言失败")
            print("错误信息为：", e)
            raise


if __name__ == '__main__':
    TestLogin().test_login()

