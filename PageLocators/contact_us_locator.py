from selenium.webdriver.common.by import By

class ContactUsLocator:
    # 联系我们或给我们留言 界面 字文案内容
    ContactUsText = (By.XPATH, '//p[text()="如果您在常见问题解答中找不到您想要的答案，可以给我们发邮件咨询。"]')

