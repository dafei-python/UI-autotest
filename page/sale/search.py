# page/sale/damai.py
from time import sleep
from common.common import Common
from conf.sale import search
from tools.get_log import GetLog
import allure

log = GetLog.get_logger()


class PageSearch(Common):
    @allure.step('输入搜索关键词')
    def page_input_search(self, keyword):
        # 获取第二个搜索输入框
        elements = self.driver.find_elements(*search.search_input)
        if len(elements) >= 2:
            elements[1].clear()
            elements[1].send_keys(keyword + "\n")

    @allure.step('点击商品')
    def page_click_goods(self):
        self.common_click(search.search_result)

    @allure.step('点击加入购物车')
    def page_click_add_cart(self):
        self.common_click(search.add_cart_btn)

    @allure.step('检查确认弹窗')
    def page_check_confirm(self):
        try:
            return self.common_find_html_element(search.confirm_modal, timeout=5)
        except:
            return False