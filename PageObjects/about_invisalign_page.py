from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.about_invisalign_locator import AboutInvisalignLocator as Aloc


class AboutInvisalignPageAssertClass:

    def assert_about_invisalign_page(self):
        # 关于Invisalign隐适美界面 获取文本文案内容 断言
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Aloc.AboutInvisalignPageText)))
        return self.driver.find_element(*Aloc.AboutInvisalignPageText).text
