from based import BasePage
from time import sleep

class Normal(BasePage):

    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)

    #后台登录
    def login(self,url,phone,password):
        page = BasePage(self.driver)
        #page.implicitly_wait(10)
        page.open(url)
        page.by_css('[placeholder="输入登录账号"]').send_keys(phone)
        page.by_css('[placeholder="输入密码"]').send_keys(password)
        page.by_css('.el-button').click()