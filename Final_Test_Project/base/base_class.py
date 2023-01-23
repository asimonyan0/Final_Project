import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.save_screenshot(
            "C:\\Users\\Armen\\PycharmProjects\\Final_Test_Project\\screen\\" + name_screenshot)  # Можно './screen/' или '.\\screen\\' . НО при запуске теста нужно находится \PycharmProjects\main_project>
        print("Screenshot Is Create")

    """Method get current URL"""
    def get_current_url(self):
        value_current_url = self.driver.current_url
        print("Current URL is " + value_current_url)

    """Method assert URL"""
    def assert_url(self, etalon_url):
        get_url = self.driver.current_url
        assert get_url == etalon_url
        print("Good Value URL")

    """Method assert word"""
    def assert_word(self, word, etalon_word):
        value_word = word.text
        assert value_word == etalon_word
        print("Good Value Word")
