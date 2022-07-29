from selenium import webdriver
from PageObjects.find_a_doctor_page import FindADoctorPage
from PageObjects.about_invisalign_page import AboutInvisalignPageAssertClass
from PageObjects.find_a_doctor_page import FindADoctorPageAssertClass
from PageObjects.the_invisalign_difference_page import TheInvisalignDifferencePageAsserClass
from PageObjects.treatment_process_page import TreatmentProcessPageAsserClass
from PageObjects.treatment_cost_page import TreatmentCostPageAsserClass
from PageObjects.tart_yinshimei_treatment_page import TartYinshimeiTreatmentPageAsserClass
from PageObjects.open_smile_test_page import OpenSmileTestPageAsserClass
from PageObjects.contact_us_page import ContactUsPageAssertClass
from PageObjects.yinshimei_experience_center_page import YinshimeiExperienceCenterAsserClass
from PageObjects.become_yinshimei_doctor_page import BecomeYinshimeiDoctorPageAssertClass
from PageObjects.organization_list_page import OrganizationListPageAsserClass
from PageObjects.index_page import IndexPage
import pytest

@pytest.mark.all()
class TestFindADoctor():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.invisalign.com.cn/find-a-doctor')

    def teardown(self):
        self.driver.quit()


    def test_01_to_index_page(self):
        # 去logo界面
        FindADoctorPage.go_invisalignlogo_index_page(self)
        # 断言 首页的图片是否存在
        IndexPage.assert_to_index_page(self)
        # 断言成功后 返回上一页 https://www.invisalign.com.cn/find-a-doctor
        self.driver.back()
        # 是否返回上一页 断言
        try:
            assert FindADoctorPageAssertClass.find_a_doctor_page_text(self) == '查找附近的 Invisalign 隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise

    def test_02_to_About_hidden_beauty_page(self):
        # 进入关于Invisalign隐适美界面
        FindADoctorPage.go_about_invisalign_page(self)
        # 断言
        try:
            assert AboutInvisalignPageAssertClass.assert_about_invisalign_page(self) == '简单三步，开启您全新的微笑之路。'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise
        # 断言成功后 返回上一页 https://www.invisalign.com.cn/find-a-doctor
        self.driver.back()
        # 是否返回上一页 断言
        try:
            assert FindADoctorPageAssertClass.find_a_doctor_page_text(self) == '查找附近的 Invisalign 隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise

    def test_03_go_teenagers_page(self):
        #进入青少年选项界面
        FindADoctorPage.go_teenagers_page(self)
        # 断言
        try:
            assert TheInvisalignDifferencePageAsserClass.assert_to_the_invisalign_difference_page(self) == '青少年'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise
        # 断言成功后 返回上一页 https://www.invisalign.com.cn/find-a-doctor
        self.driver.back()
        # 是否返回上一页 断言
        try:
            assert FindADoctorPageAssertClass.find_a_doctor_page_text(self) == '查找附近的 Invisalign 隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise

    def test_04_go_teenagers_page(self):
        #进入父母选项界面
        FindADoctorPage.go_parent_page(self)
        # 断言
        try:
            assert TheInvisalignDifferencePageAsserClass.assert_to_the_invisalign_difference_page(self) == '父母'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise
        # 断言成功后 返回上一页 https://www.invisalign.com.cn/find-a-doctor
        self.driver.back()
        # 是否返回上一页 断言
        try:
            assert FindADoctorPageAssertClass.find_a_doctor_page_text(self) == '查找附近的 Invisalign 隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise

    def test_05_go_teenagers_page(self):
        #进入成年人选项界面
        FindADoctorPage.go_adult_page(self)
        # 断言
        try:
            assert TheInvisalignDifferencePageAsserClass.assert_to_the_invisalign_difference_page(self) == '成年人'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise
        # 断言成功后 返回上一页 https://www.invisalign.com.cn/find-a-doctor
        self.driver.back()
        # 是否返回上一页 断言
        try:
            assert FindADoctorPageAssertClass.find_a_doctor_page_text(self) == '查找附近的 Invisalign 隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise

    def test_06_go_treatment_process_page(self):
        # 进入治疗过程选项界面
        FindADoctorPage.go_treatment_process_page(self)
        # 断言
        try:
            assert TreatmentProcessPageAsserClass.assert_to_treatment_process_page(self) == 'Invisalign隐适美的工作原理是什么？'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise
        # 断言成功后 返回上一页 https://www.invisalign.com.cn/find-a-doctor
        self.driver.back()
        # 是否返回上一页 断言
        try:
            assert FindADoctorPageAssertClass.find_a_doctor_page_text(self) == '查找附近的 Invisalign 隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise

    def test_07_go_treatment_cost_page(self):
        # 进入治疗过程选项界面
        FindADoctorPage.go_treatment_cost_page(self)
        # 断言
        try:
            assert TreatmentCostPageAsserClass.assert_to_treatment_cost_page(self) == '给自信加分'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise
        # 断言成功后 返回上一页 https://www.invisalign.com.cn/find-a-doctor
        self.driver.back()
        # 是否返回上一页 断言
        try:
            assert FindADoctorPageAssertClass.find_a_doctor_page_text(self) == '查找附近的 Invisalign 隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise
    def test_08_go_treatment_cost_page(self):
        # 进入开始隐适美治疗选项界面
        FindADoctorPage.go_star_yinshimei_treatment_page(self)
        # 断言
        try:
            assert TartYinshimeiTreatmentPageAsserClass.assert_to_star_yinshimei_treatment_page(self) == '寻找隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise
        # 断言成功后 返回上一页 https://www.invisalign.com.cn/find-a-doctor
        self.driver.back()
        # 是否返回上一页 断言
        try:
            assert FindADoctorPageAssertClass.find_a_doctor_page_text(self) == '查找附近的 Invisalign 隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise

    def test_09_go_looking_for_yinshimei_treatment_institution_page(self):
        # 进入寻找隐适美治疗机构选项界面
        FindADoctorPage.go_looking_for_yinshimei_treatment_institution_page(self)
        # 断言
        try:
            assert FindADoctorPageAssertClass.find_a_doctor_page_text(self) == '查找附近的 Invisalign 隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise

    def test_10_go_open_smile_test_page(self):
        # 进入开始隐适美治疗选项界面
        FindADoctorPage.go_open_smile_test_page(self)
        # 断言
        try:
            assert OpenSmileTestPageAsserClass.assert_to_open_smile_test_page(self) == '开启微笑测试'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise
        # 断言成功后 返回上一页 https://www.invisalign.com.cn/find-a-doctor
        self.driver.back()
        # 是否返回上一页 断言
        try:
            assert FindADoctorPageAssertClass.find_a_doctor_page_text(self) == '查找附近的 Invisalign 隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise

    def test_11_go_contact_us_page(self):
        # 进入联系我们或给我们留言 选项界面
        FindADoctorPage.go_contact_us_page(self)
        # 断言
        try:
            assert ContactUsPageAssertClass.assert_to_contact_us_page(self) == '如果您在常见问题解答中找不到您想要的答案，可以给我们发邮件咨询。'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise
        # 断言成功后 返回上一页 https://www.invisalign.com.cn/find-a-doctor
        self.driver.back()
        # 是否返回上一页 断言
        try:
            assert FindADoctorPageAssertClass.find_a_doctor_page_text(self) == '查找附近的 Invisalign 隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise

    def test_12_go_yinshimei_experience_center_page(self):
        # 进入隐适美体验中心  选项界面
        FindADoctorPage.go_yinshimei_experience_center_page(self)
        # 断言
        try:
            assert YinshimeiExperienceCenterAsserClass.assert_to_yinshimei_experience_center_page(self) == '上海隐适美体验中心'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise
        # 断言成功后 返回上一页 https://www.invisalign.com.cn/find-a-doctor
        self.driver.back()
        # 是否返回上一页 断言
        try:
            assert FindADoctorPageAssertClass.find_a_doctor_page_text(self) == '查找附近的 Invisalign 隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise

    def test_13_go_right_open_smile_test_page(self):
        # 进入右上角的开始微笑测试 选项界面
        FindADoctorPage.go_right_open_smile_test_page(self)
        # 断言
        try:
            assert OpenSmileTestPageAsserClass.assert_to_open_smile_test_page(self) == '开启微笑测试'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise
        # 断言成功后 返回上一页 https://www.invisalign.com.cn/find-a-doctor
        self.driver.back()
        # 是否返回上一页 断言
        try:
            assert FindADoctorPageAssertClass.find_a_doctor_page_text(self) == '查找附近的 Invisalign 隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise

    def test_14_go_right_looking_for_yinshimei_treatment_institution_page(self):
        # 进入寻找隐适美治疗机构选项界面
        FindADoctorPage.go_right_looking_for_yinshimei_treatment_institution_page(self)
        # 断言
        try:
            assert FindADoctorPageAssertClass.find_a_doctor_page_text(self) == '查找附近的 Invisalign 隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise

    def test_15_go_right_become_yinshimei_doctor_page(self):
        # 进入成为隐适美医生 选项界面
        FindADoctorPage.go_right_become_yinshimei_doctor_page(self)
        # 断言
        try:
            assert BecomeYinshimeiDoctorPageAssertClass.assert_to_become_yinshimei_doctor_page(self) == '接受 Invisalign隐适美培训，帮助更多患者!'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise
        # 断言成功后 返回上一页 https://www.invisalign.com.cn/find-a-doctor
        self.driver.back()
        # 是否返回上一页 断言
        try:
            assert FindADoctorPageAssertClass.find_a_doctor_page_text(self) == '查找附近的 Invisalign 隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise

    def test_16_go_organization_list_page(self):
        # 进入搜索结果机构列表 选项界面 测试用例
        FindADoctorPage.go_organization_list_page(self)
        # 断言
        try:
            assert OrganizationListPageAsserClass.assert_to_organization_list_page(self) == '北京大学口腔医院门诊部'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise
        # 断言成功后 返回上一页 https://www.invisalign.com.cn/find-a-doctor
        self.driver.back()
        # 是否返回上一页 断言
        try:
            assert FindADoctorPageAssertClass.find_a_doctor_page_text(self) == '查找附近的 Invisalign 隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise

    def test_17_go_advanced_optionsorganization_list_page(self):
        # 进入搜索框 高级选项 选项 配置 测试用例
        FindADoctorPage.go_advanced_options_organization_list_page(self)
        # 断言
        try:
            assert OrganizationListPageAsserClass.advanced_options_organization_list_page(self) == '首都医科大学附属北京儿童医院'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise
        # 断言成功后 返回上一页 https://www.invisalign.com.cn/find-a-doctor
        self.driver.back()
        # 是否返回上一页 断言
        try:
            assert FindADoctorPageAssertClass.find_a_doctor_page_text(self) == '查找附近的 Invisalign 隐适美治疗机构'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise

    def test_18_search_error_prompt(self):
        # 进入输入空值 点击搜索按钮 错误用例
        FindADoctorPage.search_error_prompt(self)
        # 断言
        try:
            assert FindADoctorPageAssertClass.search_error_prompt_text(self) == '请输入地址或提供者/诊所名称。'
            print("断言通过")
        except AssertionError:
            print("断言失败")
            raise

