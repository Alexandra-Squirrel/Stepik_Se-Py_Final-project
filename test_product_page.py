from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)       # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # Открываем страницу товара
    page.add_to_cart()                      # Нажимаем на кнопку "Добавить в корзину"
    page.solve_quiz_and_get_code()          # Посчитать результат математического выражения и ввести ответ
    page.should_be_the_product_in_cart()    # Название товара в сообщении совпадает с тем товаром, который добавили?
    page.should_be_correct_cost_in_cart()   # Стоимость корзины совпадает с ценой товара?

