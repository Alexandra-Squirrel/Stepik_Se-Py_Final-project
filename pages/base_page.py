import math
from .locators import BasePageLocators
from selenium import webdriver as remote_web_driver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser : remote_web_driver, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def find_element_text(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            return element.text
        except NoSuchElementException:
            return False

    # проверить, что какой-то элемент исчезает
    def is_disappeared(self, how, what, timeout=4):
        try:
            (WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what))))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    #  элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # Проверка, что подстрока "login" есть в текущем url браузера.
    def is_url_correct(self, right_substr):
        current_url = self.browser.current_url
        result = current_url.find(right_substr)
        if result == -1:
            return False
        else:
            return True

    def should_be_login_link(self):
        #  * - указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    # Посчитать результат математического выражения и ввести ответ.
    # Этот метод нужен только для проверки того, что вы написали тест на Selenium.
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")