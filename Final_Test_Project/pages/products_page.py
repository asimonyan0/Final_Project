import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Products_page(Base):               # Этот класс будет потомком класса Base.
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    locat_catalog_for_pc = "(//a[contains(text(),'Комплектующие для ПК')])[1]"       # Локатор для меню Комплектующие для ПК
    locat_basic_for_pc = "//span[contains(text(),'Основные комплектующие для ПК')]"  # Локатор для меню Основные комплектующие для ПК
    locat_ram = "//span[contains(text(),'Оперативная память')]"               # Локатор для меню Оперативная память
    locat_dimm = "//span[contains(text(),'Оперативная память DIMM')]"         # Локатор для меню Оперативная память DIMM
    locat_ddr3 = "//a[normalize-space()='DDR3']"                              # Локатор для просмотра DDR3
    locat_sort = "//span[@class='top-filter__selected'][contains(text(),'Сначала недорогие')]" # Локатор для меню сортировки
    locat_most_popular = "//span[contains(text(),'Сначала популярные')]"      # Локатор для сортировки Сначала популярные
    locat_first_product = "//body/div[@class='container category-child']/div[@class='products-page']/div[@class='products-page__content']/div[@class='products-page__list']/div[@class='products-list']/div[@class='products-list__content']/div[@class='catalog-products view-simple']/div[1]/a[1]/span[1]"  # Локатор для выбора первого продукта
    locat_add_to_cart = "//button[contains(text(),'Купить')]"                 # Локатор для добавления товара в корзину
    locat_go_to_cart = "//span[@class='buttons__link-icon cart-link-counter__icon']"  # Локатор для кнопки Перейти в корзину

    # Getters
    def get_catalog_for_pc(self):      # Будет возвращать значение, для обращения к меню Комплектующие для ПК
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.locat_catalog_for_pc)))
    def get_basic_for_pc(self):        # Будет возвращать значение, для обращения к меню Основные комплектующие
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.locat_basic_for_pc)))
    def get_ram(self):                 # Будет возвращать значение, для обращения к меню Оперативная память
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.locat_ram)))
    def get_dimm(self):                # Будет возвращать значение, для обращения к меню Оперативная память DIMM
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.locat_dimm)))
    def get_ddr3(self):                # Будет возвращать значение, для просмотра DDR3
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.locat_ddr3)))
    def get_sort(self):                # Будет возвращать значение, для меню сортировки
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.locat_sort)))
    def get_most_popular(self):        # Будет возвращать значение, для сортировки Сначала популярные
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.locat_most_popular)))
    def get_first_product(self):       # Будет возвращать значение, для выбора первого продукта
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.locat_first_product)))
    def get_add_to_cart(self):         # Будет возвращать значение, для добавления в корзину
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.locat_add_to_cart)))
    def get_go_to_cart(self):          # Будет возвращать значение, для перехода в корзину
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.locat_go_to_cart)))

    # Actions
    def click_catalog_for_pc(self):
        self.get_catalog_for_pc().click()     # Будет нажать на меню Комплектующие для ПК
        print("Click Catalog For PC")
    def click_basic_for_pc(self):
        self.get_basic_for_pc().click()       # Будет нажать на меню Основные комплектующие
        print("Click Basic For PC")
    def click_ram(self):
        self.get_ram().click()                # Будет нажать на меню Оперативная память
        print("Click RAM")
    def click_dimm(self):
        self.get_dimm().click()               # Будет нажать на меню Оперативная память DIMM
        print("Click DIMM")
    def click_ddr3(self):
        self.get_ddr3().click()               # Будет нажать на кнопку фильтр DDR3
        print("Click DDR3")
    def click_sort(self):
        self.get_sort().click()               # Будет нажать на меню сортировки
        print("Click Sort")
    def click_most_popular(self):
        self.get_most_popular().click()       # Будет нажать на кнопку, для сортировки Сначала популярные
        print("Click Most Popular")
    def click_first_product(self):
        self.get_first_product().click()      # Будет нажать на кнопку, для выбора первого продукта
        print("Click First Product")
    def click_add_to_cart(self):
        self.get_add_to_cart().click()        # Будет нажать на кнопку, для добавления в корзину
        print("Click Add To Cart")
    def click_go_to_cart(self):
        self.get_go_to_cart().click()         # Будет нажать на кнопку, для перехода в корзину
        print("Click Go To Cart")

    # Methods
    def select_ram_1(self):
        self.click_catalog_for_pc()       # Будет нажать на меню Комплектующие для ПК
        self.click_basic_for_pc()         # Будет нажать на меню Основные комплектующие
        self.click_ram()                  # Будет нажать на меню Оперативная память
        self.click_dimm()                 # Будет нажать на меню Оперативная память DIMM
        self.click_ddr3()                 # Будет нажать на кнопку фильтр DDR3
        self.click_sort()                 # Будет нажать на меню сортировки
        self.click_most_popular()         # Будет нажать на кнопку, для сортировки Сначала популярные
        time.sleep(2)
        self.click_first_product()        # Будет нажать на кнопку, для выбора первого продукта
        time.sleep(2)
        self.click_add_to_cart()          # Будет нажать на кнопку, для добавления в корзину
        time.sleep(2)
        self.click_go_to_cart()           # Будет нажать на кнопку, для перехода в корзину
        time.sleep(2)
