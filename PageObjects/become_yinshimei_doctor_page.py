from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.become_yinshimei_doctor_locator import BecomeYinshimeiDoctorLocator as Bloc

class BecomeYinshimeiDoctorPageAssertClass:

    def assert_to_become_yinshimei_doctor_page(self):
        # 成为隐适美医生 文本文案
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Bloc.BecomeYinshimeiDoctorText)))
        return self.driver.find_element(*Bloc.BecomeYinshimeiDoctorText).text
