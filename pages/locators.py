from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group > a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    # товар в корзине
    BASKET_ITEM = (By.CLASS_NAME, "basket-items")
    # текст о том, что корзина пуста
    NO_ITEM_TEXT = (By.CSS_SELECTOR, "#content_inner > p > a")

class MainPageLocators:
    LOGIN_LINK_2 = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_INPUT_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    TITLE_OF_PRODUCT = (By.CSS_SELECTOR, "div.product_main > h1")
    ADDED_TO_CART_TITLE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > .price_color") # 23,99 £
    CART_COST_MESSAGE = (By.CSS_SELECTOR, "#messages > div > div > p:nth-child(1) > strong") # 23,99 £
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

