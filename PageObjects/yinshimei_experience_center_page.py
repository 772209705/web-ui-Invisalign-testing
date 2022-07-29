from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.yinshimei_experience_center_locator import YinshimeiExperienceCenterLocator as Yloc

class YinshimeiExperienceCenterAsserClass:

    def assert_to_yinshimei_experience_center_page(self):
        # 隐适美体验中心界面 文本文案内容 断言
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((Yloc.YinshimeiExperienceCenterText)))
        return self.driver.find_element(*Yloc.YinshimeiExperienceCenterText).text
