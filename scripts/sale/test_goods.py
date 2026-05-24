import os

from tools.get_driver import GetDriver
from tools.read_json import read_json
from page.sale.login import PageLogin
from tools.get_log import GetLog
from page.sale.goods import Goods

log = GetLog.get_logger()
import allure


@allure.feature("商户添加商品类")
class TestGoods:
    # 初始化
    log.info("初始化")

    def setup_class(self):
        # 初始化登录json数据
        pathdir = os.sep + "sale" + os.sep + "login.json"
        self.data_json = read_json(pathdir)
        # 初始化添加商品json数据
        json_path = os.sep + "sale" + os.sep + "goods.json"
        self.goods_data = read_json(json_path)

        # 初始化driver
        self.driver = GetDriver().get_driver(self.data_json[0])
        # 调用登录方法
        PageLogin(self.driver).page_login(self.data_json[1], self.data_json[2])
        # 调用添加商品类
        self.goods = Goods(self.driver)

    # 结束
    log.info("结束")

    def teardown_class(self):
        self.driver.quit()

    # 调用page层的综合调用方法
    log.info("调用page层的综合调用方法")

    @allure.title("添加商品方法")
    def test_goods(self):
        self.goods.page_goods(self.goods_data[0], self.goods_data[1], self.goods_data[2], self.goods_data[3],
                              self.goods_data[4], self.goods_data[5], self.goods_data[6], self.goods_data[7])
        # 避免因为错误导致脚本异常中断
        try:
            # 判断是否添加成功
            log.info("断言成功")
            assert self.goods.goods_stus() == self.goods_data[8]
        # 未成功，抛出异常
        except Exception as e:
            log.info("断言失败")
            print("错误信息为：", e)
            raise


if __name__ == '__main__':
    TestGoods().test_goods()
