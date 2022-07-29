from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.treatment_process_locator import TreatmentProcessLocator as Tloc

class TreatmentProcessPageAsserClass:

    def assert_to_treatment_process_page(self):
        # 治疗过程界面的文本文案
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((Tloc.TreatmentProcessText)))
        return self.driver.find_element(*Tloc.TreatmentProcessText).text
