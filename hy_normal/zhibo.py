#coding=UTF-8
import time
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from based import BasePage

class zhiboPage(BasePage):
    '''直播页面封装'''
    def __init__(self,driver):
        self.driver = driver
        self.page = BasePage(self.driver)
        driver.implicitly_wait(30)
        url='https://service-wbs321.newtamp.cn/passport/saas/index.html#/'
        self.page.open(url)
        sleep(2)
        self.page.by_css('[placeholder="输入登录账号"]').send_keys('17343057927')
        self.page.by_css('[placeholder="输入密码"]').send_keys('000000a')
        self.page.by_css('.el-button').click()
        sleep(5)
        self.page.open('https://service-wbs321.newtamp.cn/live')
        sleep(5)
#        self.page.open('https://hy-service.newtamp.cn/dashboard?token=undefined')
#        sleep(2)
#        self.page.open('https://hy-service.newtamp.cn/dashboard?token=123')
#        sleep(2)
#        sleep(2)

        driver.implicitly_wait(10)

     #新增按钮
    def insert_button(self):
        self.driver.implicitly_wait(20)
        self.driver.refresh()
        self.page.by_class('before-btn').click()

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
        #切换进富文本
        neirong = self.page.by_css('#tinymce')
#        neirong.click()
        neirong.send_keys(keys)
        # 返回原有frame

        self.driver.switch_to_default_content()
        print('富文本已编辑')
        sleep(2)
        self.page.by_css('.title-pop>div>section:nth-child(2)').click()
        print('富文本已保存')

    #分享配置
    def select_fxpz(self,css):
        print('分享配置start')
        if css == "启用":
            print('启用状态')
            self.page.by_css(".el-radio-group>.el-radio:first-child>span").click()
        else:
            print('禁用状态')
            self.page.by_css(".el-radio-group>.el-radio:nth-child(2)>span").click()

    #新增直播
    def insertzhibo(self,fenlei_child,zhibo_title,zhibo_sub,pic_url,zhibo_fwb,fxpz):
        #点击新增按钮
        self.insert_button()
        # 选择直播分类
        self.select_button(fenlei_child,".form-center-wrapper>.el-form-item:first-child>div>div>.flex-wrapper")
        now_time = str(int(time.time()))
        # 直播标题
        self.input_text('[placeholder="最多100个字"]',zhibo_title)
        # 直播开始时间
        self.select_data('.today')
        #直播简介
        self.input_text('[placeholder="最多100字"]',zhibo_sub)
        # 上传图片
        self.fs_picture(pic_url)
        sleep(3)
        # 直播内容介绍
        self.input_fwb("iframe[id = 'tinymce_ifr']",zhibo_fwb)
        print('直播内容ok')
        # 直播状态
  #      self.select_button(zhibo_status)
        #分享配置
        self.select_fxpz(fxpz)
        print('分享配置ok')

        #保存
        self.page.by_css('.self-footer>.nb-button-wrapper:nth-child(2)').click()
  #      self.driver.close()

    #查看未发布的直播详情
    def weifabudetailzb(self):
        # 跳转至直播列表页,并切换到未发布列表
        # 查看第一个直播
        self.driver.refresh()
        sleep(2)
        gx = self.page.by_css('.el-table__row:nth-child(1)>td:nth-child(2)>.cell')
        return gx.text

    #查看已发布的直播详情
    def fabudetailzb(self):
        self.driver.refresh()
        self.page.by_css('#tab-1').click()
        gx = self.page.by_css('.el-table__row:nth-child(1)>td:nth-child(2)>.cell')
        return gx.text

    #发布直播
    def fabuzb(self):
        self.page.by_css('#tab-2').click()
        sleep(2)
        weifabu_title = self.page.by_css('.el-table__row:nth-child(1)>td:nth-child(2)>.cell')

        gx = self.page.by_css('.el-table__row:nth-child(1)>td:nth-child(1)>.cell>.el-checkbox')
        ActionChains(self.driver).move_to_element(gx).click().perform()

        sleep(2)
        # 发布直播
        # driver.find_element_by_css_selector('.batch-wrapper>.btn-item').click()
        self.page.by_css('.batch-wrapper:first-child>div:nth-child(2)>span:nth-child(2)').click()

        # 确定发布直播,接收警告框
        # driver.switch_to.alert.accept()
        self.page.by_css('.el-message-box__btns>button:nth-child(2)').click()
        return weifabu_title

    #撤销发布直播
    def cxfabuzb(self):
        self.page.by_css('#tab-1').click()
        sleep(2)
        fabu_title = self.page.by_css('.el-table__row:nth-child(1)>td:nth-child(2)>.cell')

        gx = self.page.by_css('.el-table__row:nth-child(1)>td:nth-child(1)>.cell>.el-checkbox')
        ActionChains(self.driver).move_to_element(gx).click().perform()
        sleep(2)
        # 撤销发布直播
        self.page.by_css('.batch-wrapper:first-child>div:nth-child(3)>span:nth-child(2)').click()

        # 确定撤销发布直播,接收警告框
        # driver.switch_to.alert.accept()
        self.page.by_css('.el-message-box__btns>button:nth-child(2)').click()
        return fabu_title

    #置顶直播
    def zhiding(self):
        self.page.by_css('#tab-1').click()
        sleep(2)
        zd_title = self.page.by_css('.el-table__row:nth-child(1)>td:nth-child(2)>.cell')

        gx = self.page.by_css('.el-table__row:nth-child(1)>td:nth-child(1)>.cell>.el-checkbox')
        ActionChains(self.driver).move_to_element(gx).click().perform()
        sleep(2)
        # 撤销发布直播
        self.page.by_css('.batch-wrapper:first-child>div:nth-child(2)>span:nth-child(2)').click()

        # 确定撤销发布直播,接收警告框
        # driver.switch_to.alert.accept()
        self.page.by_css('.el-message-box__btns>button:nth-child(2)').click()
        return zd_title

    #查看置顶title
    def zd_title(self):
        try:
            zd_logo = self.page.by_css('.el-table__row:first-child>td:nth-child(2)>div.cell>a>div.el-badge>sup')
            zd_title = self.page.by_css('.el-table__row:first-child>td:nth-child(2)>div.cell>a').title

        except:
            print("无置顶内容")

        finally:
            return zd_title


    #搜索直播标题
    def search_zbtitle(self):
        self.page.by_css('#tab-1').click()
        find = self.page.by_css('.el-table__header>thead>tr>th:nth-child(2)>div.cell>div.header-wrapper>section')
        ActionChains(self.driver).move_to_element(find).perform()

        self.page.by_xpath(('[placeholder="搜索关键字"]')).send_keys('直播标题')
        self.page.by_css('.button-wrapper:nth-child(2)>button.el-button--primary').click()



