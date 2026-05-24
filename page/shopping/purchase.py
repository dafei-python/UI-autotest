# -*- coding:utf-8 -*-
# @Author:大飞记Python
# @Time:2024/7/17
# @Functiong: 购物脚本
from time import sleep

from common.common import Common
from conf.shopping import purchase
import allure


class PagePurchase(Common):

    # 1、输入“iPhone14 PIus”
    @allure.step('输入“iPhone14 PIus”')
    def page_pur_input(self, value):
        self.common_input(purchase.pur_input, value)

    # 2、点击“搜索”
    @allure.step('')
    def page_pur_search(self):
        self.common_click(purchase.pur_search)

    # 3、选择 第一个商品
    @allure.step('')
    def page_pur_chose(self):
        self.common_click(purchase.pur_chose)

    # 4、选择“iPhone14 PIus 紫色”
    @allure.step('选择“iPhone14 PIus 紫色”')
    def page_pur_Purple(self):
        self.common_turn_table(-1)
        sleep(1)
        self.common_click(purchase.pur_Purple)

    # 5、选择“1TB”
    @allure.step('选择“1TB”')
    def page_pur_onetb(self):
        self.common_click(purchase.pur_onetb)

    # 6、点击“加入购物车”
    @allure.step('点击“加入购物车”')
    def page_pur_go_purchase(self):
        self.common_click(purchase.pur_go_purchase)

    # 7、点击“去购物车结算”
    @allure.step('点击“去购物车结算”')
    def page_pur_Checkout(self):
        self.common_click(purchase.pur_Checkout)

    # 8、点击“去结算”
    @allure.step('点击“去结算”')
    def page_pur_go_Checkout(self):
        self.common_click(purchase.pur_go_Checkout)

    # 9、点击“提交订单”
    @allure.step('点击“提交订单”')
    def page_pur_orders(self):
        self.common_click(purchase.pur_orders)

    # 10、点击“支付宝支付”
    @allure.step('点击“支付宝支付”')
    def page_pur_alipay(self):
        self.common_click(purchase.pur_alipay)

    # 11、点击“支付成功”
    @allure.step('点击“支付成功”')
    def page_pur_pay_ok(self):
        self.common_click(purchase.pur_pay_ok)

    # 12、点击“查看订单”
    @allure.step('点击“查看订单”')
    def page_pur_check_orders(self):
        self.common_click(purchase.pur_check_orders)

    # 13、获取商品手机信息
    @allure.step('获取商品手机信息')
    def page_pur_get_info(self):
        return self.common_get_word(purchase.pur_get_info)

    # 14、点击“取消订单”
    @allure.step('点击“取消订单”')
    def page_pur_cancel_ordres(self):
        self.common_click(purchase.pur_cancel_ordres)

    # 15、点击“确定”
    @allure.step('点击“确定”')
    def page_pur_cancel_ok(self):
        self.common_click(purchase.pur_cancel_ok)

    # 16、获取订单状态
    @allure.step('获取订单状态')
    def page_pur_get_status(self):
        return self.common_get_word(purchase.pur_get_status)

    # 综合调用方法
    @allure.step('综合调用方法')
    def page_purchase(self, shops):
        self.page_pur_input(shops)
        sleep(2)
        self.page_pur_search()
        sleep(2)
        self.page_pur_chose()
        sleep(2)
        self.page_pur_Purple()
        sleep(2)
        self.page_pur_onetb()
        sleep(2)
        self.page_pur_go_purchase()
        sleep(2)
        self.page_pur_Checkout()
        sleep(2)
        self.page_pur_go_Checkout()
        sleep(2)
        self.page_pur_orders()
        sleep(2)
        self.page_pur_alipay()
        sleep(2)
        self.page_pur_pay_ok()
        sleep(2)
        self.page_pur_check_orders()
        sleep(2)
        self.page_pur_get_info()
        sleep(2)
        self.page_pur_cancel_ordres()
        sleep(2)
        self.page_pur_cancel_ok()
        sleep(2)
        self.page_pur_get_status()
