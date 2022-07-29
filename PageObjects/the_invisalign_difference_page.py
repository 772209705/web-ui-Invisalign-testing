from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.the_invisalign_difference_locator import TheInvisalignDifferenceLocator as Tloc

class TheInvisalignDifferencePageAsserClass:

    def assert_to_the_invisalign_difference_page(self):
        # 青少年等待蓝色框元素出现
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((Tloc.button)))
        return self.driver.find_element(*Tloc.button).text
