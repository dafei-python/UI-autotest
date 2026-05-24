# -*- coding:utf-8 -*-
# @Author:大飞记Python
# @Time:2024/7/30 10:16
# @Functiong:
from common.common import Common
from conf.sale import goods
from time import sleep
import allure


class Goods(Common):
    # 点击“商品发布”
    @allure.step("点击“商品发布”")
    def goods_fabu(self):
        self.common_click(goods.fabu)

    # 选择“虚拟产品”
    @allure.step("选择“虚拟产品”")
    def goods_xuni(self):
        self.common_click(goods.xuni)

    # 点击“确认”
    @allure.step("点击“确认”")
    def goods_sure(self):
        self.common_click(goods.sure)

    # 选择“汽车用品”
    @allure.step("选择“汽车用品”")
    def goods_car(self):
        self.common_click(goods.car)

    # 选择“整车”
    @allure.step("选择“整车”")
    def goods_all_car(self):
        self.common_click(goods.all_car)

    # 选择“新车”
    @allure.step("选择“新车”")
    def goods_new_car(self):
        self.common_click(goods.new_car)

    # 选择“下一步”
    @allure.step("选择“下一步”")
    def goods_next(self):
        self.common_click(goods.next)

    # 输入“商品名称”
    @allure.step("入“商品名称”")
    def goods_name(self, name):
        self.common_input(goods.goods_name, name)

    # 输入“商品价格”
    @allure.step("输入“商品价格”")
    def goods_prize(self, prize):
        self.common_input(goods.goods_prize, prize)

    # 输入“商品卖点”
    @allure.step("输入“商品卖点”")
    def goods_text(self, text):
        self.common_input(goods.goods_text, text)

    # 选择“计量单位”
    @allure.step("选择“计量单位”")
    def goods_danwei(self):
        self.common_click(goods.goods_danwei)

    # 选择“台”
    @allure.step("选择“台”")
    def goods_tai(self):
        self.common_click(goods.goods_tai)

    # 点击“上传图片”
    @allure.step("点击“上传图片”")
    def goods_pic(self):
        self.common_down_page(goods.goods_pic)
        sleep(1)
        self.common_click(goods.goods_pic)

    # 选择“第一张图片”
    @allure.step("选择“第一张图片”")
    def goods_chose_pic(self):
        self.common_click(goods.goods_chose_pic)

    # 点击“添加规格项”
    @allure.step("点击“添加规格项”")
    def goods_guige(self):
        self.common_click(goods.goods_guige)

    # 输入“规格项名称”
    @allure.step("输入“规格项名称”")
    def goods_guige_name(self, guige_name):
        self.common_input(goods.goods_guige_name, guige_name)

    # 输入“规格值”
    @allure.step("输入“规格值”")
    def goods_guige_number(self, guige_value):
        self.common_input(goods.goods_guige_number, guige_value)

    # 输入“价格”
    @allure.step("输入“价格”")
    def goods_guige_prize(self, guize_prize):
        self.common_input(goods.goods_guige_prize, guize_prize)

    # 输入“库存”
    @allure.step("输入“库存”")
    def goods_guige_num(self, guige_num):
        self.common_input(goods.goods_guige_num, guige_num)

    # 输入“货品号”
    @allure.step("输入“货品号”")
    def goods_guige_code(self, guige_code):
        self.common_input(goods.goods_guige_code, guige_code)

    # 点击“保存商品”
    @allure.step("点击“保存商品”")
    def goods_save(self):
        self.common_click(goods.goods_save)

    # 点击“去店铺查看商品列表”
    @allure.step("点击“去店铺查看商品列表”")
    def goods_go_shopping(self):
        self.common_click(goods.goods_go_shopping)

    # 输入“商品名称”
    @allure.step("输入“商品名称”")
    def input_goods_name(self, name):
        self.common_input(goods.input_goods_name, name)

    # 点击“搜索”
    @allure.step("点击“搜索”")
    def search_goods(self):
        self.common_click(goods.search_goods)

    # 获取“商品上架状态”
    @allure.step("获取“商品上架状态”")
    def goods_stus(self):
        return self.common_get_word(goods.get_goods_stus)

    # 综合调用方法
    def page_goods(self, goods_name, prize, text, guige_name, guige_number, guige_prize, guige_num, guige_code):
        sleep(2)
        self.goods_fabu()
        sleep(1)
        self.goods_xuni()
        sleep(1)
        self.goods_sure()
        sleep(1)
        self.goods_car()
        sleep(1)
        self.goods_all_car()
        sleep(1)
        self.goods_new_car()
        sleep(1)
        self.goods_next()
        sleep(1)
        self.goods_name(goods_name)
        sleep(1)
        self.goods_prize(prize)
        sleep(1)
        self.goods_text(text)
        sleep(1)
        self.goods_danwei()
        sleep(1)
        self.goods_tai()
        sleep(1)
        self.goods_pic()
        sleep(1)
        self.goods_chose_pic()
        sleep(1)
        self.goods_guige()
        sleep(1)
        self.goods_guige_name(guige_name)
        sleep(1)
        self.goods_guige_number(guige_number)
        sleep(1)
        self.goods_guige_prize(guige_prize)
        sleep(1)
        self.goods_guige_num(guige_num)
        sleep(1)
        self.goods_guige_code(guige_code)
        sleep(1)
        self.goods_save()
        sleep(1)
        self.goods_go_shopping()
        sleep(1)
        self.input_goods_name(goods_name)
        sleep(1)
        self.search_goods()
        sleep(1)
        self.goods_stus()
