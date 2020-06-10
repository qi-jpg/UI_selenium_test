#coding=UTF-8
import time

class BasePage:
    '''基础的selenium定位方法'''

    def __init__(self,driver):
        self.driver = driver

    #打开页面
    def open(self,url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    #id定位
    def by_id(self,id):
        return self.driver.find_element_by_id(id)

    #name定位
    def by_name(self,name):
        return self.driver.find_element_by_name(name)

    #class定位
    def by_class(self,class_name):
        return self.driver.find_element_by_class_name(class_name)

    #Xpath定位
    def by_xpath(self,xpath):
        return self.driver.find_element_by_xpath(xpath)

    #css定位
    def by_css(self,css):
        return self.driver.find_element_by_css_selector(css)

    #获取title
    def get_title(self):
        return self.driver.title

    #获取页面text,（使用xpath)定位
    def get_text(self,xpath):
        return self.by_xpath(xpath).text

    #执行javascript脚本
    def js(self,script):
        self.driver.execute_script(script)

    #执行点击事件
    def click(self):
        self.driver.click()
        time.sleep(2)