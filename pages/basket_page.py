from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def go_to_basket(self):
        # метод для добавления в корзину
        basket_btn = self.browser.find_element(*BasketPageLocators.BASKET_BTN)
        basket_btn.click()

    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), \
            "items is in basket, but should not be"

