from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.index_locator import IndexLocator as Iloc

class IndexPage:

    def assert_to_index_page(self):
        # 等待该页面的图片出现，如不出现则出错了
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Iloc.indexImg)))
