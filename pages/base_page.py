from selenium import webdriver as remote_web_driver

class BasePage:
    def __init__(self, browser: remote_web_driver, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)