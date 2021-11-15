from .base_page import BasePage
from selenium import webdriver
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        login_text_in_url = 'login' in self.browser.current_url
        assert login_url and login_text_in_url, "Login link or 'login' text in link is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "REGISTER FORM is not presented"

    def register_new_user(self, email, password):
        # который принимает две строки и регистрирует пользователя.
        # Реализуйте его, описав соответствующие элементы страницы.
        email_register_user = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER)
        password1_register_user = self.browser.find_element(*LoginPageLocators.PASSWORD1_REGISTER)
        password2_register_user = self.browser.find_element(*LoginPageLocators.PASSWORD2_REGISTER)
        btn_register_user = self.browser.find_element(*LoginPageLocators.BTN_REGISTER_USER)
        email_register_user.send_keys(email)
        password1_register_user.send_keys(password)
        password2_register_user.send_keys(password)
        btn_register_user.click()


