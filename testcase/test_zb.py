#coding=UTF-8
import unittest
from selenium import webdriver
#import sys
#sys.path.append("/Users/maimai/Desktop/UI_selenium_test/hy_normal/")
#import zhibo
#import normal
from hy_normal import zhibo
from hy_normal import normal
from ddt import ddt,data,unpack
import time
'''
import zhibo
import normal
'''
'''
import sys
import os
cur_directory = os.path.dirname(os.path.dirname(__file__))
root_path = os.path.abspath(os.path.dirname(cur_directory)+os.path.sep+".")
sys.path.append(root_path)
from hy_normal.zhibo import zhiboPage
'''

@ddt
class TestZhiBo(unittest.TestCase):

    @classmethod  #不需要实例化
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        normal.login()

    now_time=str(int(time.time()))
    @data({"fenlei":'.el-select:first-child','fenlei_child':'.el-select-dropdown__item:nth-child(6)','zhibo_title':'直播标题'+now_time,'zhibo_sub':'直播简介',
           'pic_url':"/Users/maimai/Desktop/mamen.png",'zhibo_fwb':'这里是富文本','zhibo_status':'.self-footer>.nb-button-wrapper:nth-child(2)','fxpz':'.el-radio:nth-child(2)>.el-radio__inner'})
    @unpack
    def test_insertzhibo(self,fenlei,fenlei_child,zhibo_title,zhibo_sub,pic_url,zhibo_fwb,zhibo_status,fxpz):

        zb = zhibo.zhiboPage(self.driver)
        zb.insertzhibo(fenlei,fenlei_child,zhibo_title,zhibo_sub,pic_url,zhibo_fwb,zhibo_status,fxpz)
        text = zb.detailzb()
        print(text)
        self.assertEqual("直播标题",text)

    def test_fabuzhibo(self):
        zb = zhibo.zhiboPage(self.driver)



    @classmethod
    def tearDownClass(cls):
        pass
#        cls.driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity=2)  #测试结果会显示详细信息