from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import Cart_page
from pages.client_info_page import Client_info
from pages.main_page import Main_page
from pages.products_page import Products_page


def test_buy_ram():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    print("Start Test Buy RAM")

    mp = Main_page(driver)
    mp.select_full_catalog_products()

    pp = Products_page(driver)
    pp.select_ram_1()

    cp = Cart_page(driver)
    cp.making_order()

    ip = Client_info(driver)
    ip.input_info()

    print("Finish Test Buy RAM")
    driver.close()