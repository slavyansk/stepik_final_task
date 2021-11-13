from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    ADD_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_PRODUCT = (By.TAG_NAME, "h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")  
    ADD_BASKET_ALERT = (By.CSS_SELECTOR, ".alertinner strong")
    ADD_BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info p strong")