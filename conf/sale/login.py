# 存放前端HTML的元素
from selenium.webdriver.common.by import By

# 用户名
username = By.CSS_SELECTOR, ("[placeholder='请输入用户名']")
# 密码
password = By.CSS_SELECTOR, ("[placeholder='请输入密码']")
# 登录按钮
login_btn = By.XPATH, ('//*[@id="main"]/div/div/div/div[2]/div[2]/div')
# 拼接小缺口图片
small_pic = By.XPATH, ('//*[@id="main"]/div/div/div/div[4]/div[1]/img[2]')
# 拼接背景图
big_pic = By.XPATH, ('//*[@id="main"]/div/div/div/div[4]/div[1]/img[1]')
# 拼接滑块
picture_btn = By.XPATH, ('//*[@id="main"]/div/div/div/div[4]/div[2]/span[2]')
# 登录后文字
get_word = By.XPATH, ('//*[@id="main"]/div/div[3]/div/div/div[1]/div[2]/h4')
