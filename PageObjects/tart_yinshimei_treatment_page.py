from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.tart_yinshimei_treatment_locator import TartYinshimeiTreatmentLocator as Tloc

class TartYinshimeiTreatmentPageAsserClass:

    def assert_to_star_yinshimei_treatment_page(self):
        # 开始隐适美治疗界面的文本文案
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Tloc.TartYinshimeiTreatmentButtonText)))
        return self.driver.find_element(*Tloc.TartYinshimeiTreatmentButtonText).text
