# conf/sale/damai.py
from selenium.webdriver.common.by import By

search_input = By.CSS_SELECTOR, '[placeholder="输入你想查找的商品"]'
search_result = By.CLASS_NAME, "goods-show-info"
add_cart_btn = By.CSS_SELECTOR, ".ivu-btn.ivu-btn-warning"
confirm_modal = By.CLASS_NAME, "ivu-modal-confirm-head-title"