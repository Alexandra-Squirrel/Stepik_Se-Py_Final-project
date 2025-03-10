from .base_page import BasePage

# Класс-предок в Python указывается в скобках:
class MainPage(BasePage):
    pass

    # или так:
    # def __init__(self, *args, **kwargs):
    #     super(MainPage, self).__init__(*args, **kwargs)