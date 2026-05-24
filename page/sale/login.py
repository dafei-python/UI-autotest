from time import sleep

from common.common import Common
from conf.sale import login
from tools.make_picture import Make_Picture
from tools.get_log import GetLog
import allure

log = GetLog.get_logger()

# 商城登录类
log.info("商城登录类")


class PageLogin(Common):
    # 输入用户名
    log.info("输入用户名")

    @allure.step('输入用户名')
    def page_input_username(self, username):
        self.common_input(login.username, username)

    # 输入密码
    log.info("输入密码")

    @allure.step('输入密码')
    def page_input_password(self, password):
        self.common_input(login.password, password)

    # 点击登录
    log.info("点击登录")

    @allure.step('点击登录')
    def page_click_login_btn(self):
        self.common_click(login.login_btn)

    # 验证滑块
    log.info("验证滑块")

    @allure.step('验证滑块')
    def page_save_picture(self):
        # 保存滑动验证图片至本地
        lld = self.common_save_picture(login.small_pic, login.big_pic)
        sleep(1)
        # 计算要滑动的距离
        dirt = Make_Picture().Measure_distance(lld[0], lld[1])
        sleep(1)
        # 拖动滑块完成验证
        self.common_hold_mouse(login.picture_btn, dirt, 0)
        sleep(1)

    # 获取登录成功后文字
    log.info("获取登录成功后文字")

    @allure.step('获取登录成功后文字')
    def page_get_word(self):
        return self.common_get_word(login.get_word)

    # 综合调用方法
    log.info("综合调用方法")

    @allure.step('综合调用方法')
    def page_login(self, username='13011111111', password='111111'):
        sleep(2)
        self.page_input_username(username)
        sleep(1)
        self.page_input_password(password)
        sleep(2)
        self.page_click_login_btn()
        sleep(2)
        self.page_save_picture()
