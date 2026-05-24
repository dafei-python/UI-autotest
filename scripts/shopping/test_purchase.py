# -*- coding:utf-8 -*-
# @Author:大飞记Python
# @Time:2024/11/04
# @Functiong: 购物脚本
import allure
import pytest

from tools.get_driver import GetDriver
from tools.read_json import read_json
from page.shopping.login import PageLogin
from page.shopping.purchase import PagePurchase


@allure.feature('购物自动化脚本类')
class TestPurchase:
    # 初始化
    def setup_class(self):
        # 初始化数据
        self.data = read_json("purchase.json")
        # 初始化驱动
        self.driver = GetDriver().get_driver(self.data[0])
        # 调用登录方法
        PageLogin(self.driver).page_login(self.data[1], self.data[2])

    # 关闭driver
    def teardown_class(self):
        self.driver.quit()

    # 购物脚本类
    @pytest.mark.repeat(2)
    @allure.title('购物自动化方法')
    def test_purchase(self):
        PagePurchase(self.driver).page_purchase(self.data[3])
        try:
            assert PagePurchase(self.driver).page_pur_get_info() == self.data[4]
        except Exception as e:
            print("错误信息为：", e)
            raise
        # 回到首页，方便第2次脚本运行
        self.driver.get(self.data[5])


if __name__ == '__main__':
    TestPurchase().test_purchase()
