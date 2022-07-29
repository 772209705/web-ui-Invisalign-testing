from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.contact_us_locator import ContactUsLocator as Cloc

class ContactUsPageAssertClass:

    def assert_to_contact_us_page(self):
        # 联系我们或给我们留言 文本文案
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Cloc.ContactUsText)))
        return self.driver.find_element(*Cloc.ContactUsText).text
