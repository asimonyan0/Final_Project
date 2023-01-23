import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Client_info(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    locat_phon_number = "(//input[@id='ir-5fg6jf'])[1]"  # Локатор для добавления номера телефона
    locat_email = "(//input[@id='ir-vaxj2u'])[1]"  # Локатор для добавления Email
    locat_pickup = "//div[@class='checkout-getting']//div[@class='base-tabs__wrapper']//div[1]"  # Локатор для кнопки Самовывоз
    locat_select_shop = "//span[contains(text(),'Выбрать магазин')]"     # Локатор для меню выбора магазина
    locat_shop_1 = "(//button[@loading='false'])[7]"                     # Локатор для выбора магазина
    locat_payment_method = "//*[@id='checkout']/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]"  # Локатор для выбора способа оплаты
    locat_select_sberpay = "//div[contains(text(),'SberPay')]"            # Локатор для выбора SberPay
    locat_confirm_order = "//span[contains(text(),'Подтвердить заказ')]"  # Локатор для подтверждения заказа

    # Getters
    def get_phon_number(self):          # Будет возвращать значение для добавления номера телефона
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locat_phon_number)))
    def get_email(self):                # Будет возвращать значение для добавления Email
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locat_email)))
    def get_pickup(self):               # Будет возвращать значение для кнопки Самовывоз
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locat_pickup)))
    def get_select_shop(self):          # Будет возвращать значение для меню выбора магазина
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locat_select_shop)))
    def get_shop_1(self):               # Будет возвращать значение для выбора магазина 1
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locat_shop_1)))
    def get_payment_method(self):       # Будет возвращать значение для выбора способа оплаты
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locat_payment_method)))
    def get_select_sberpay(self):       # Будет возвращать значение для выбора SberPay
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locat_select_sberpay)))
    def get_confirm_order(self):        # Будет возвращать значение для подтверждения заказа
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locat_confirm_order)))

    # Actions
    def input_phon_number(self, phon_number):  # Будет вводить значение, в поле добавления номера телефона
        self.get_phon_number().send_keys(phon_number)
        print("Input Phon Number")
    def input_email(self, email):              # Будет вводить значение, в поле добавления Email
        self.get_email().send_keys(email)
        print("Input Email")
    def click_pickup(self):                    # Будет нажать на кнопку Самовывоз
        self.get_pickup().click()
        print("Click Pickup")
    def click_select_shop(self):               # Будет нажать на меню выбора магазина
        self.get_select_shop().click()
        print("Click Select Shop")
    def click_shop_1(self):                    # Будет нажать на кнопку выбора магазина 1
        self.get_shop_1().click()
        print("Click Shop 1")
    def click_payment_method(self):            # Будет нажать на кнопку выбора способа оплаты
        self.get_payment_method().click()
        print("Click Payment Method")
    def click_select_sberpay(self):            # Будет нажать на кнопку выбора SberPay
        self.get_select_sberpay().click()
        print("Click Select Sberpay")
    def click_confirm_order(self):            # Будет нажать на кнопку подтверждения заказа
        self.get_confirm_order().click()
        print("Click Confirm Order")

    # Methods
    def input_info(self):
        # time.sleep(3)
        # self.input_phon_number("7777777777") # Будет вводить значение, в поле добавления номера телефона
        # time.sleep(3)
        # self.input_email("Test@mail.ru")     # Будет вводить значение, в поле добавления Email
        time.sleep(3)
        self.click_pickup()                  # Будет нажать на кнопку Самовывоз
        time.sleep(3)
        self.click_select_shop()             # Будет нажать на меню выбора магазина
        time.sleep(3)
        self.click_shop_1()                  # Будет нажать на кнопку выбора магазина 1
        time.sleep(3)
        self.click_payment_method()          # Будет нажать на кнопку выбора способа оплаты
        self.click_select_sberpay()          # Будет нажать на кнопку выбора SberPay
        self.click_confirm_order()           # Будет нажать на кнопку подтверждения заказа
        self.get_screenshot()                # Будет сделать скриншот экрана