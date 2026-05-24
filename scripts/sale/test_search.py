# scripts/sale/test_damai.py
import os
import pytest
from tools.get_driver import GetDriver
from tools.read_json import read_json
from page.sale.search import PageSearch
from tools.get_log import GetLog
import allure

log = GetLog.get_logger()


@allure.epic("LILISHOP商城购物系统")
@allure.feature("商品搜索模块")
class TestSearch:
    def setup_class(self):
        pathdir = os.sep + "sale" + os.sep + "damai.json"
        self.data = read_json(pathdir)
        self.driver = GetDriver().get_driver(self.data[0])
        self.search = PageSearch(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @allure.story("商品搜索流程")
    @allure.title("搜索并添加商品测试")
    def test_search_flow(self):
        # 执行搜索操作
        self.search.page_input_search(self.data[1])

        # 切换新窗口
        self.search.common_turn_table(-1)

        # 点击商品
        self.search.page_click_goods()

        # 再次切换新窗口
        self.search.common_turn_table(-1)

        # 点击加入购物车
        self.search.page_click_add_cart()

        # 断言验证
        assert self.search.page_check_confirm(), "确认弹窗未出现"

        # 等待5秒
        self.search.driver.implicitly_wait(5)


if __name__ == "__main__":
    pytest.main(["-s", "test_damai.py"])