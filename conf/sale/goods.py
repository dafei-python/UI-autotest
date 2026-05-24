# -*- coding:utf-8 -*-
# @Author:大飞记Python
# @Time:2024/7/30 10:17
# @Functiong:
from selenium.webdriver.common.by import By

fabu = By.XPATH, "//*[text()=' 商品发布 ']"
xuni = By.XPATH, "//*[text()='虚拟商品']"
sure = By.XPATH, "//*[text()='确定']"
car = By.XPATH, "//*[text()='汽车用品']"
all_car = By.XPATH, "//*[text()='整车']"
new_car = By.XPATH, "//*[text()='新车']"
next = By.XPATH, "//*[text()='下一步']"
goods_name = By.XPATH, '//*[@id="main"]/div/div[3]/div/div/div[3]/div[1]/form/div/div[1]/div[2]/div/div/input'
goods_prize = By.XPATH, '//*[@id="main"]/div/div[3]/div/div/div[3]/div[1]/form/div/div[1]/div[3]/div/div/input'
goods_text = By.XPATH, '//*[@id="main"]/div/div[3]/div/div/div[3]/div[1]/form/div/div[1]/div[4]/div/div/textarea'
goods_danwei = By.XPATH, "//*[text()='请选择']"
goods_tai = By.XPATH, "//*[text()='台 ']"
goods_pic = By.XPATH, "//*[text()='上传图片']"
goods_chose_pic = By.CSS_SELECTOR, ".card"
goods_guige = By.XPATH, "//*[text()='添加规格项 ']"
goods_guige_name = By.CSS_SELECTOR, '[placeholder="请输入规格项名称"]'
goods_guige_number = By.CSS_SELECTOR, '[placeholder="请输入规格值"]'
goods_guige_prize = By.CSS_SELECTOR, '[placeholder="请输入价格"]'
goods_guige_num = By.CSS_SELECTOR, '[placeholder="请输入库存"]'
goods_guige_code = By.CSS_SELECTOR, '[placeholder="请输入货号"]'
goods_save = By.XPATH, "//*[text()=' 保存商品 ']"
goods_go_shopping = By.XPATH, "//*[text()='去店铺查看商品列表>>']"
input_goods_name = By.CSS_SELECTOR, '[placeholder="请输入商品名称"]'
search_goods = By.XPATH, "//*[text()='搜索']"
get_goods_stus = By.XPATH, '//*[@id="main"]/div/div[3]/div/div/div/div/div[3]/div[1]/div[2]/table/tbody/tr/td[9]/div/div/span'
