from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.organization_list_locator import OrganizationListLocator as Oloc

class OrganizationListPageAsserClass:

    def assert_to_organization_list_page(self):
        # 搜索结果 机构列表 的文本文案 提取
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Oloc.OrganizationListText)))
        return self.driver.find_element(*Oloc.OrganizationListText).text

        # 高级选项 面试 搜索 机构列表 西单
    def advanced_options_organization_list_page(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Oloc.AdvancedOptionsOrganizationListText)))
        return self.driver.find_element(*Oloc.AdvancedOptionsOrganizationListText).text

