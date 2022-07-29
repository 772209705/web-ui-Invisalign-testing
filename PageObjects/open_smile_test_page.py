from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.open_smile_test_locator import OpenSmileTestLocator as Oloc

class OpenSmileTestPageAsserClass:

    def assert_to_open_smile_test_page(self):
        # 开启微笑测试界面 的文本文案
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Oloc.OpenSmileTestText)))
        return self.driver.find_element(*Oloc.OpenSmileTestText).text
