from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from base.base_class import Base

class Cart_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    locat_plus_button = "//i[@class='count-buttons__icon count-buttons__icon-plus']"       # Локатор для добавления такого же товара
    locat_making_order = "//button[@id='buy-btn-main']"                                    # Локатор для перехода к оформлению товаров
    locat_text_cart = "//h1[contains(text(),'Корзина')]"                                   # Локатор для основного текста страницы

    # Getters
    def get_plus_button(self):   # Будет возвращать значение, для добавления такого же товара
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locat_plus_button)))
    def get_making_order(self):  # Будет возвращать значение, для перехода к оформлению товаров
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locat_making_order)))
    def get_text_cart(self):     # Будет возвращать значение, для основного текста страницы
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locat_text_cart)))

    # Actions
    def click_plus_button(self):
        self.get_plus_button().click()    # Будет нажать на кнопку добавления такого же товара
        print("Click Plus Button")
    def click_making_order(self):
        self.get_making_order().click()   # Будет нажать на кнопку, для перехода к оформлению товаров
        print("Click Making Order")

    # Methods
    def making_order(self):
        self.assert_word(self.get_text_cart(), "Корзина")  # Проверка текста на странице
        time.sleep(2)
        self.click_plus_button()                           # Будет нажать на кнопку добавления такого же товара
        time.sleep(2)
        self.click_making_order()                          # Будет нажать на кнопку, для перехода к оформлению товаров

