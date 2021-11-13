from .base_page import BasePage
from selenium import webdriver
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        # метод для добавления в корзину
        add_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BTN)
        add_basket_btn.click()


    def should_be_add_to_basket_message(self):
        # Сообщение о том, что товар добавлен в корзину.Название товара в сообщении должно совпадать
        # с тем товаром, который вы действительно добавили
        alert_message = self.browser.find_element(*ProductPageLocators.ADD_BASKET_ALERT)
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        assert name_product.text == alert_message.text, "message name product incorrect!!!"

    def should_be_price_equal_in_basket(self):
        # Cообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        price_alert_message = self.browser.find_element(*ProductPageLocators.ADD_BASKET_PRICE)
        assert price.text == price_alert_message.text, "price message is incorrect!"

