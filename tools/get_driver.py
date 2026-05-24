from selenium import webdriver
from tools.get_log import GetLog

log = GetLog.get_logger()

# driver驱动类
log.info("driver驱动类")


class GetDriver:
    # 设置driver
    log.info("设置driver")
    driver = None

    # 启动浏览器驱动
    log.info("启动浏览器驱动方法")

    def get_driver(self, url):
        # 判断是否为空
        log.info("判断是否为空")
        if self.driver is None:
            # 为空，启动浏览器驱动
            log.info("为空，启动浏览器驱动")
            self.driver = webdriver.Chrome()
            # 最大化
            log.info("最大化")
            self.driver.maximize_window()
            # 打开url
            log.info("打开url为：" + str(url))
            self.driver.get(url)
            # 返回driver
            log.info("返回driver")
            return self.driver

    # 关闭浏览器
    log.info("关闭浏览器")

    def quit_driver(self):
        # 判断是否为空
        log.info("判断是否为空")
        if self.driver:
            # 不为空，关闭driver
            log.info("不为空，关闭driver")
            self.driver.quit()
            # 置空数据
            log.info("置空数据")
            self.driver = None

