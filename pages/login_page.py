from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input_1 = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_1)
        password_input_1.send_keys(password)
        password_input_2 = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_2)
        password_input_2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    #------------------------------------------------------------
    def should_be_login_url(self):
        assert self.is_url_correct("login"), "Login link is not contains 'login' in it"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
