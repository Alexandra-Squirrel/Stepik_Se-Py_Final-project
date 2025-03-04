import math
from selenium import webdriver as remote_web_driver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class BasePage:
    def __init__(self, browser : remote_web_driver, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def find_element_text(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            return element.text
        except NoSuchElementException:
            return False

    # Проверка, что подстрока "login" есть в текущем url браузера.
    def is_url_correct(self, right_substr):
        current_url = self.browser.current_url
        result = current_url.find(right_substr)
        if result == -1:
            return False
        else:
            return True

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