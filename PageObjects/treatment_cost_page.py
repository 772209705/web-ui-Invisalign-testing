from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.treatment_cost_locator import TreatmentCostLocator as Tloc

class TreatmentCostPageAsserClass:

    def assert_to_treatment_cost_page(self):
        # 治疗费用界面的文本文案
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Tloc.TreatmentCostText)))
        return self.driver.find_element(*Tloc.TreatmentCostText).text
