from based import BasePage
from time import sleep

class Normal(BasePage):

    def login(self,url):
        page = BasePage(self.driver)
        page.open(url)
        sleep(2)
        page.open(url)
