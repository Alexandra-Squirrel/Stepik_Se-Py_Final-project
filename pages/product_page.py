from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_btn.click()

    def should_be_the_product_in_cart(self):
        # 1) Сообщение о том, что товар добавлен в корзину.
        # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        product_in_cart = self.find_element_text(*ProductPageLocators.ADDED_TO_CART_TITLE)
        product_in_page = self.find_element_text(*ProductPageLocators.TITLE_OF_PRODUCT)
        assert product_in_page == product_in_cart, "The product in the cart is incorrect"

    def should_be_correct_cost_in_cart(self):
        # 2) Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        cost_in_cart = self.find_element_text(*ProductPageLocators.CART_COST_MESSAGE)
        product_price = self.find_element_text(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price == cost_in_cart, "The cost in cart is incorrect"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), ("Success message is presented, "
                                                                                   "but should not be")

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), ("Success message is presented, "
                                                                                   "but should disappeared")
