from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from base.base_class import Base


class Main_page(Base):                # Этот класс будет потомком класса Base.
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = 'https://www.dns-shop.ru/'  # Будем обращатся к url отсюда

    # Locators
    locat_catalog_products = "//span[@class='header-bottom__catalog-spoiler']" # Локатор для меню каталога товаров
    locat_search_field = "//input[@placeholder='Поиск по сайту']"              # Локатор для поле поиска товаров
    locat_enter_city = "//span[@class='city-select__text_BTU']"                # Локатор для меню выбора города
    locat_samara = "//a[contains(text(),'Самара')]"                            # Локатор для выбора города Самара

    # Getters
    def get_catalog_products(self):    # Будет возвращать значение, для обращения к меню каталога товаров
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.locat_catalog_products)))
    def gets_search_field(self):       # Будет возвращать значение, для обращения к полю поиска товаров
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.locat_search_field)))
    def get_enter_city(self):          # Будет возвращать значение, для обращения к полю выбора города
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.locat_enter_city)))
    def get_enter_samara(self):        # Будет возвращать значение, для выбора города Самара
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.locat_samara)))


    # Actions
    def click_catalog_products(self):        # Будет нажать на меню каталога товаров
        self.get_catalog_products().click()
        print("Click Catalog Products")
    def click_enter_city(self):              # Будет нажать на меню выбора города
        self.get_enter_city().click()
        print("Click Enter City")
    def click_enter_samara(self):            # Будет выбрать город Самара
        self.get_enter_samara().click()
        print("Click Enter Samara")

    # Methods
    def select_full_catalog_products(self):
        self.driver.get(self.url)                     # Открываем страницу с помощью url, который прописан в начале
        self.get_current_url()                        # Будет печатать нынешный URL
        self.assert_url("https://www.dns-shop.ru/")   # Будет сравнить нынешный URL с эталоном
        self.driver.maximize_window()
        self.click_catalog_products()                 # Будет нажать на меню каталога товаров
        self.click_enter_city()                       # Будет нажать на меню выбора город
        self.click_enter_samara()                     # Будет выбрать город Самара
        time.sleep(2)

