from selenium.webdriver.common.by import By

class OrganizationListLocator:
    # 搜索机构列表界面文本元素 北京大学口腔医院门诊部
    OrganizationListText = (By.XPATH, '//p[text()="北京大学口腔医院门诊部"]')
    # 高级选项 搜索 西单 机构列表元素  首都医科大学附属北京儿童医院
    AdvancedOptionsOrganizationListText = (By.XPATH, '//p[text()="首都医科大学附属北京儿童医院"]')

