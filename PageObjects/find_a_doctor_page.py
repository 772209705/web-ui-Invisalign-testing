from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.find_a_doctor_locator import findADoctor_locator as Floc
from PageLocators.index_locator import IndexLocator as Iloc

class FindADoctorPage:

    def go_invisalignlogo_index_page(self):
        # 等待并点击logo进入首页界面
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.invisalignLogo)))
        self.driver.find_element(*Floc.invisalignLogo).click()

    def go_about_invisalign_page(self):
        # 进入关于Invisalign隐适美界面
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.AboutInvisalignButton)))
        self.driver.find_element(*Floc.AboutInvisalignButton).click()

    def go_teenagers_page(self):
        # 进入青少年界面
        #鼠标悬停操作
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.Special)))
        ele = self.driver.find_element(*Floc.Special)
        ActionChains(self.driver).move_to_element(ele).perform()
        # 进入青少年界面
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.Teenagers)))
        self.driver.find_element(*Floc.Teenagers).click()

    def go_parent_page(self):
        # 进入青少年界面
        # 鼠标悬停操作
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.Special)))
        ele = self.driver.find_element(*Floc.Special)
        ActionChains(self.driver).move_to_element(ele).perform()
        # 进入青少年界面
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.Parent)))
        self.driver.find_element(*Floc.Parent).click()

    def go_adult_page(self):
        # 进入青少年界面
        # 鼠标悬停操作
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.Special)))
        ele = self.driver.find_element(*Floc.Special)
        ActionChains(self.driver).move_to_element(ele).perform()
        # 进入青少年界面
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.Adult)))
        self.driver.find_element(*Floc.Adult).click()

    def go_treatment_process_page(self):
        # 进入治疗过程界面
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.TreatmentProcess)))
        self.driver.find_element(*Floc.TreatmentProcess).click()

    def go_treatment_cost_page(self):
        # 进入治疗费用界面
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.TreatmentCost)))
        self.driver.find_element(*Floc.TreatmentCost).click()

    def go_star_yinshimei_treatment_page(self):
        # 进入开始隐适美治疗界面
        # 鼠标悬停操作
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.StartYinshimeiTreatment)))
        ele = self.driver.find_element(*Floc.StartYinshimeiTreatment)
        ActionChains(self.driver).move_to_element(ele).perform()
        # 进入开始隐适美治疗界面
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.tartYinshimeiTreatment)))
        self.driver.find_element(*Floc.tartYinshimeiTreatment).click()

    def go_looking_for_yinshimei_treatment_institution_page(self):
        # 进入寻找隐适美治疗机构界面
        # 鼠标悬停操作
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.StartYinshimeiTreatment)))
        ele = self.driver.find_element(*Floc.StartYinshimeiTreatment)
        ActionChains(self.driver).move_to_element(ele).perform()
        # 进入寻找隐适美治疗机构界面
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.LookingForYinshimeiTreatmentInstitution)))
        self.driver.find_element(*Floc.LookingForYinshimeiTreatmentInstitution).click()

    def go_open_smile_test_page(self):
        # 进入开始微笑测试 界面
        # 鼠标悬停操作
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.StartYinshimeiTreatment)))
        ele = self.driver.find_element(*Floc.StartYinshimeiTreatment)
        ActionChains(self.driver).move_to_element(ele).perform()
        # 进入开始微笑测试 界面
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((Floc.openSmileTest)))
        self.driver.find_element(*Floc.openSmileTest).click()

    def go_contact_us_page(self):
        # 进入联系我们或给我们留言 界面
        # 鼠标悬停操作
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.StartYinshimeiTreatment)))
        ele = self.driver.find_element(*Floc.StartYinshimeiTreatment)
        ActionChains(self.driver).move_to_element(ele).perform()
        # 进入联系我们或给我们留言 界面
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((Floc.contactUs)))
        self.driver.find_element(*Floc.contactUs).click()

    def go_yinshimei_experience_center_page(self):
        # 进入隐适美体验中心 界面
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((Floc.YinshimeiExperienceCenter)))
        self.driver.find_element(*Floc.YinshimeiExperienceCenter).click()

    def go_right_open_smile_test_page(self):
        # 进入右上角的开始微笑测试 界面
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((Floc.RightOpenSmileTest)))
        self.driver.find_element(*Floc.RightOpenSmileTest).click()

    def go_right_looking_for_yinshimei_treatment_institution_page(self):
        # 进入右上角的寻找隐适美治疗机构 界面
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((Floc.RightLookingForYinshimeiTreatmentInstitution)))
        self.driver.find_element(*Floc.RightLookingForYinshimeiTreatmentInstitution).click()

    def go_right_become_yinshimei_doctor_page(self):
        # 进入右上角的成为隐适美医生 界面
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((Floc.RightBecomeYinshimeiDoctor)))
        self.driver.find_element(*Floc.RightBecomeYinshimeiDoctor).click()

    def go_organization_list_page(self):
        # 进入搜索的机构列表 界面
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((Floc.AddressInput)))
        self.driver.find_element(*Floc.AddressInput).send_keys('西单')
        self.driver.find_element(*Floc.SearchButton).click()

    def go_advanced_options_organization_list_page(self):
        # 进入搜索的机构列表 界面 选项操作高级选项
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((Floc.AddressInput)))
        self.driver.find_element(*Floc.AddressInput).send_keys('西单')
        # 点击高级选项
        self.driver.find_element(*Floc.AdvancedOptions).click()
        # 断言
        try:
            text = FindADoctorPageAssertClass.advanced_options_find_a_doctor_page(self)
            assert text[0] == '诊所'
            print("诊所断言通过")
            assert text[1] == '10'
            print("距离断言通过")
        except AssertionError:
            print("诊所、距离断言失败")
            raise
        # 输入儿童
        self.driver.find_element(*Floc.PracticeName).send_keys('儿童')
        self.driver.find_element(*Floc.Radius).click()
        # 下拉框
        self.driver.find_element(*Floc.RadiusValue).click()
        # 提供微笑模拟
        self.driver.find_element(*Floc.ProvideSmileSimulation).click()
        # 搜索按钮
        self.driver.find_element(*Floc.SearchButton).click()

    def search_error_prompt(self):
        # 搜索按钮
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((Floc.SearchButton)))
        self.driver.find_element(*Floc.SearchButton).click()


class FindADoctorPageAssertClass:

    def find_a_doctor_page_text(self):
        # 查找附近的 Invisalign 隐适美治疗机构
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.InvisalignText)))
        return self.driver.find_element(*Floc.InvisalignText).text

    def advanced_options_find_a_doctor_page(self):
        # 高级选项 诊所 和 距离 值
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.PracticeName)))
        text1 = self.driver.find_element(*Floc.PracticeName).get_attribute('placeholder')
        text2 = self.driver.find_element(*Floc.Radius).get_attribute('value')
        return text1,text2

    def search_error_prompt_text(self):
        # 搜索按钮 错误提示信息 获取
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((Floc.ErrorPrompt)))
        return self.driver.find_element(*Floc.ErrorPrompt).text
