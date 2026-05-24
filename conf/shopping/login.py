# 存放前端HTML的元素
from selenium.webdriver.common.by import By

# 用户名
username = By.CSS_SELECTOR, ("[placeholder='用户名']")
# 密码
password = By.CSS_SELECTOR, ("[placeholder='密码']")
# 登录按钮
login_btn = By.XPATH, ('//*[@id="app"]/div/div[2]/div[2]/div[3]/div[1]/form[1]/div[3]/div/button')
# 拼接小滑块
small_pic = By.XPATH, ('//*[@id="app"]/div/div[2]/div[3]/div[1]/img[1]')
# 拼接背景图
big_pic = By.XPATH, ('//*[@id="app"]/div/div[2]/div[3]/div[1]/img[2]')
# 拼接滑块
picture_btn = By.XPATH, ('//*[@id="app"]/div/div[2]/div[3]/div[2]/span[2]')
# 登录后文字
get_word = By.XPATH, ('//*[@id="app"]/div/div[3]/div/ul[1]/ul/li[1]')
