from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_nothing_in_basket(self):
        self.should_be_no_product_in_basket()
        self.should_be_text_about_empty_basket()

    # Ожидаем, что в корзине нет товаров
    def should_be_no_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), ("Basket item is presented, "
                                                                                   "but should not be")

    # Ожидаем, что есть текст о том что корзина пуста
    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.NO_ITEM_TEXT), "Text about empty basket is not presented"
