from selenium.webdriver.common.by import By

class findADoctor_locator:
    # logo
    invisalignLogo = (By.CSS_SELECTOR, '[class="d-inline-block align-top invis-black-logo"]')
    # 查找附近机构文本内容
    InvisalignText = (By.CSS_SELECTOR, '[class="dl-welcome-header"]')
    # find a doctor 界面的关于Invisalign隐适美 按钮
    AboutInvisalignButton = (By.CSS_SELECTOR, '[class="dropdown-toggle nav-link"]')
    # 隐适美的特别之处 元素
    Special = (By.XPATH, '//span[text()="隐适美的特别之处 "]')
    # 青少年按钮 元素
    Teenagers =(By.CSS_SELECTOR, '[class="class_teens_sub_menu dropdown-item"]')
    # 父母按钮 元素
    Parent = (By.CSS_SELECTOR, '[class="class_parents_sub_menu dropdown-item"]')
    # 成年人按钮 元素
    Adult = (By.CSS_SELECTOR, '[class="class_adults_sub_menu dropdown-item"]')
    # 治疗过程 元素
    TreatmentProcess=(By.CSS_SELECTOR, '[class="dropdown-toggle nav-link"][href="/treatment-process"]')
    # 治疗费用 元素
    TreatmentCost = (By.CSS_SELECTOR, '[class="dropdown-toggle nav-link"][href="/invisalign-cost"]')
    # 开始隐适美治疗悬停 元素
    StartYinshimeiTreatment = (By.XPATH, '//span[text()="开始隐适美治疗"]')
    # 开始隐适美治疗 按钮元素
    tartYinshimeiTreatment = (By.CSS_SELECTOR, '[class="class_get_inv dropdown-item"]')
    # 寻找隐适美治疗机构
    LookingForYinshimeiTreatmentInstitution = (By.CSS_SELECTOR, '[class="class_find_a_doctor_sub_menu dropdown-item"]')
    # 开启微笑测试 按钮元素
    openSmileTest = (By.CSS_SELECTOR, '[class="class_take_smile_assessment_sub_menu dropdown-item"]')
    # 联系我们或给我们留言
    contactUs= (By.CSS_SELECTOR, '[class="class_contact_us_sub_menu dropdown-item"]')
    # 隐适美体验中心
    YinshimeiExperienceCenter = (By.CSS_SELECTOR, '[class="dropdown-toggle nav-link"][href="/invisalign-centre"]')
    # 右上角大字开始微笑测试
    RightOpenSmileTest = (By.CSS_SELECTOR, '[class="header-links"]>[class="fad"]>[class="sa-link"]')
    # 右上角的寻找隐适美治疗机构
    RightLookingForYinshimeiTreatmentInstitution = (By.CSS_SELECTOR, '[data-telium-event="fad_home_page_serach"]')
    # 成为隐适美医生
    RightBecomeYinshimeiDoctor = (By.CSS_SELECTOR, '[data-telium-event="for_doctor_header"]')
    # 地址输入框
    AddressInput = (By.ID, 'amap-city-input')
    # 寻找隐适美治疗机构按钮
    SearchButton = (By.CSS_SELECTOR, '[class="btn btn-dark-border btn-full transparent"]')
    # 高级选项功能 元素
    AdvancedOptions = (By.CSS_SELECTOR, '[class="dl-white"]')
    # 选项一 诊所
    PracticeName =(By.ID, 'practicename-input')
    # 选项二
    Radius = (By.CSS_SELECTOR, '[name="radius"][class="dl-input "]')
    RadiusValue = (By.CSS_SELECTOR, '[value="20"]')
    # 提供微笑模拟
    ProvideSmileSimulation = (By.CSS_SELECTOR, '[class="slider round"]')
    # 搜索按钮为空 错误提示信息 请输入地址或提供者/诊所名称。
    ErrorPrompt = (By.CSS_SELECTOR, '[class="dl-error-msg"]')





