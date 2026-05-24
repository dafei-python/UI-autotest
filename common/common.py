import base64
import time
from selenium.webdriver import ActionChains
import os
from conftest import BASE_PATH

from selenium.webdriver.support.wait import WebDriverWait
from tools.get_log import GetLog

log = GetLog.get_logger()


class Common:
    log.info("调用初始化driver方法")

    # 初始化driver
    def __init__(self, driver):
        self.driver = driver

    # 查找元素（设置显式等待，防止前端元素未加载成功造成的错误）
    log.info("调用查找元素方法")

    def common_find_html_element(self, loc, timeout=60, poll=0.5):
        """
        :param loc: 元素定位
        :param timeout: 等待时长
        :param poll: 查找间隔
        :return:
        """
        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x: x.find_element(*loc)))

    # 点击方法
    log.info("调用点击方法")

    def common_click(self, loc):
        """
        :param loc: 元素定位
        :return:
        """
        log.info("正在点击" + str(loc) + "元素")
        self.common_find_html_element(loc).click()

    # 输入方法
    log.info("调用输入方法")

    def common_input(self, loc, value):
        """

        :param loc: 元素定位
        :param value: 输入值
        :return:
        """
        # 查找输入元素
        log.info("查找输入" + str(loc) + "元素")
        temp = self.common_find_html_element(loc)
        # 置空输入框
        log.info("置空输入框")
        temp.clear()
        # 输入数值
        log.info("输入数值" + value)
        temp.send_keys(value)

    # 加密图片，解码并保存本地
    log.info("调用加密图片，解码并保存本地方法")

    def common_save_picture(self, loc, lodc):
        """

        :param loc: 背景图图元素定位
        :param lodc: 贴块元素定位
        :return:
        """
        # 获取图片元素定位
        log.info("获取图片元素定位" + str(loc))
        pic = self.common_find_html_element(loc)
        pidc = self.common_find_html_element(lodc)
        # 获取图片的加密地址
        log.info("获取图片的加密地址")
        ss = pic.get_attribute("src")
        sds = pidc.get_attribute("src")
        # 拆分成加密为base64常规格式
        log.info("拆分成加密为base64常规格式")
        numbers = ss.split(",")
        numberds = sds.split(",")
        # 获取图片的base64加密数据
        log.info("获取图片的base64加密数据")
        djd = numbers[1]
        djdd = numberds[1]
        # base64解码
        log.info("base64解码")
        lk = base64.b64decode(djd)
        lkd = base64.b64decode(djdd)
        # 图片保存路径
        pic_path = BASE_PATH + os.sep + "result" + os.sep + "image" + os.sep + "big" + ".png"
        pidc_path = BASE_PATH + os.sep + "result" + os.sep + "image" + os.sep + "samll" + ".png"
        log.info("背景图片保存路径{},拼接图片保存路径{}".format(pic_path, pidc_path))
        # 图片保存本地
        log.info("图片保存本地")
        sav = open(pic_path, "wb")
        sadv = open(pidc_path, "wb")
        sav.write(lk)
        sadv.write(lkd)
        # 关闭
        log.info("关闭保存的图片")
        sav.close()
        sadv.close()
        return pic_path, pidc_path

    # 按住鼠标左键并拖动，然后释放鼠标
    log.info("调用按住鼠标左键并拖动，然后释放鼠标方法")

    def common_hold_mouse(self, loc, xoffset, yoffset):
        """
        :param loc: 元素定位
        :param xoffset: 横向移动距离
        :param yoffset: 纵向移动距离
        :return:
        """
        # 获取元素定位
        log.info("获取元素定位" + str(loc))
        bcv = self.common_find_html_element(loc)
        # 按住按钮
        log.info("按住对应元素" + str(loc))
        ActionChains(self.driver).click_and_hold(bcv).perform()
        time.sleep(1)
        # 滑动距离对应距离
        log.info("滑动横向距离：{}，纵向距离：{}".format(xoffset, yoffset))
        ActionChains(self.driver).move_by_offset(xoffset, yoffset).perform()
        time.sleep(1)
        # 释放鼠标
        log.info("释放鼠标")
        ActionChains(self.driver).release().perform()

    # 获取文字
    log.info("调用获取文字方法")

    def common_get_word(self, loc):
        """

        :param loc: 元素定位
        :return:
        """
        # 获取文字的元素定位
        log.info("获取文字的元素定位" + str(loc))
        huy = self.common_find_html_element(loc)
        # 返回文字
        log.info("返回文字")
        return huy.text

    # 切换页面句柄
    log.info("切换页面句柄")

    def common_turn_table(self, num):
        """

        :param num: 窗口角标 (-1切换到最新打开的窗口;0切换到最开始打开的窗口)
        :return:
        """
        # 获取当前浏览器的所有窗口句柄
        log.info("#获取当前浏览器的所有窗口句柄")
        handles = self.driver.window_handles
        print(handles)
        # 切换到窗口
        log.info("切换到窗口")
        self.driver.switch_to.window(handles[num])

    # 滑动页面至可见元素
    log.info("滑动页面至可见元素")

    def common_down_page(self, loc):
        """
        :param loc: 元素定位
        :return:
        """
        element = self.common_find_html_element(loc)
        # 滑动页面至可见元素
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)

