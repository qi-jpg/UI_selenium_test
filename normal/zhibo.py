#coding=UTF-8
import time
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from based import BasePage

class zhiboPage(BasePage):
    '''直播页面封装'''
    def __init__(self,driver):
        self.driver = driver
        url='https://hy-service.newtamp.cn/live/liveManage'
        self.page = BasePage(self.driver)
        self.page.open('https://hy-service.newtamp.cn/dashboard?token=undefined')
        sleep(2)
        self.page.open('https://hy-service.newtamp.cn/dashboard?token=123')
        sleep(2)
        self.page.open(url)
        sleep(2)
        driver.implicitly_wait(10)

     #新增按钮
    def insert_button(self):
        self.page.by_class('before-btn').click()
        '''
        WebDriverWait(self.page,5,0.5).until(
            EC.visibility_of_element_located(By.CSS_SELECTOR,'[placeholder="最多100个字"]'),message='未加载成功'
        )
    '''
    #下拉框选择
    def select_button(self,child,css=None):
        if css:
            self.page.by_css(css).click()
        self.page.by_css(child).click()

    #输入文本
    def input_text(self,css,keys):
        self.page.by_css(css).send_keys(keys)

    #选择日期控件
    def select_data(self,day):
        self.page.by_css('[placeholder="选择日期时间"]').click()
        sleep(2)
        self.page.by_css(day).click()
        self.page.by_css('.el-button--default').click()

    #上传图片
    def fs_picture(self,url):
        self.page.by_id('fs-picture').send_keys(url)

    #编辑富文本
    def input_fwb(self,ifame,keys):
        self.page.by_css('.editor-btn').click()
        self.driver.implicitly_wait(10)
        self.driver.switch_to.frame(self.page.by_css(ifame))
        self.driver.implicitly_wait(10)
        #切换进富文本
        neirong = self.page.by_css('#tinymce')
#        neirong.click()
        neirong.send_keys(keys)
        # 返回原有frame
        self.driver.switch_to_default_content()
        self.page.by_css('.title-pop>div>section:nth-child(2)').click()


    #新增直播
    def insertzhibo(self,fenlei,fenlei_child,zhibo_title,zhibo_sub,pic_url,zhibo_fwb,zhibo_status):
        #点击新增按钮
        self.insert_button()
        # 选择直播分类
#        self.select_button('.el-select-dropdown__item:nth-child(6)','.el-select:first-child')
        self.select_button(fenlei_child,fenlei)
        now_time = str(int(time.time()))
        # 直播标题
        self.input_text('[placeholder="最多100个字"]',zhibo_title)
        # 直播开始时间
        self.select_data('.today')
        #直播简介
        self.input_text('[placeholder="最多100字"]',zhibo_sub)
        # 上传图片
        self.fs_picture(pic_url)

        # 直播内容介绍
        self.input_fwb("iframe[id = 'tinymce_ifr']",zhibo_fwb)
        # 直播状态
        self.select_button(zhibo_status)
        self.page.by_css('.self-footer>.nb-button-wrapper:nth-child(2)').click()

  #      self.driver.close()

    #查看未发布的直播详情
    def detailzb(self):
        # 跳转至直播列表页,并切换到未发布列表
        # 查看第一个直播
        gx = self.page.by_css('.el-table__row:nth-child(1)>td:nth-child(2)>.cell')
        return gx.text
