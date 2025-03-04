from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_2 = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators:
    # should_be_login_url
    # should_be_login_form
    # should_be_register_form
    # LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    TITLE_OF_PRODUCT = (By.CSS_SELECTOR, "div.product_main > h1")
    ADDED_TO_CART_TITLE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > .price_color") # 23,99 £
    CART_COST_MESSAGE = (By.CSS_SELECTOR, "#messages > div > div > p:nth-child(1) > strong") # 23,99 £

