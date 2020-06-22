#coding=UTF-8
import unittest
from selenium import webdriver
import sys
sys.path.append("/Users/maimai/Desktop/UI_selenium_test/hy_normal/")
#import zhibo

from ddt import ddt, data, unpack, file_data
import time

#from hy_normal import zhibo
from zhibo import zhiboPage
from normal import Normal

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
        print()


 #   @data({"fenlei":'.el-select:first-child','fenlei_child':'.el-select-dropdown__item:nth-child(6)','zhibo_title':'直播标题'+now_time,'zhibo_sub':'直播简介',
 #          'pic_url':"/Users/maimai/Desktop/mamen.png",'zhibo_fwb':'这里是富文本','zhibo_status':'.self-footer>.nb-button-wrapper:nth-child(2)',
 #          'fxpz':'.el-radio:nth-child(2)>.el-radio__inner','now_time':now_time})
 #   @unpack
    #新增直播
    @file_data('/Users/maimai/Desktop/UI_selenium_test/data/zb_insert.json')
    def test_insertzhibo(self,fenlei_child,zhibo_title,zhibo_sub,pic_url,zhibo_fwb,fxpz):
        zb = zhiboPage(self.driver)
        now_time=str(int(time.time()))
        zhibo_title = zhibo_title + now_time
        zb.insertzhibo(fenlei_child,zhibo_title,zhibo_sub,pic_url,zhibo_fwb,fxpz)
        text = zb.weifabudetailzb()
        self.assertEqual("直播标题"+now_time,text)


    #发布直播
    @unittest.skip('跳过测试')
    def test_fabuzhibo(self):
        zb = zhiboPage(self.driver)
        zb.fabuzb()
        text = zb.fabudetailzb()
        print(text)
        weifabu = zb.weifabudetailzb()
        print(weifabu)

        self.assertEqual(weifabu,text)

    #撤销发布直播
    @unittest.skip('跳过测试')
    def test_cxfabuzhibo(self):
        zb = zhiboPage(self.driver)
        zb.cxfabuzb()
        text = zb.fabudetailzb()
        print("打算撤销发布的直播名称",text)

        fabu = zb.weifabudetailzb()
        print("撤销发布的直播名称",fabu)
        self.assertEqual(text,fabu)

    #置顶直播
    @unittest.skip('跳过测试')
    def test_zhiding(self):
        zb  = zhiboPage(self.driver)
        text = zb.fabudetailzb()
        zb.zhiding()
        zd_title = zb.zd_title()
        self.assertEqual(text,zd_title)

    #搜索直播标题
    @unittest.skip('跳过测试')
    def test_search_zbtitle(self):
        zb = zhiboPage(self.driver)
        keys = '直播'
        nums = zb.search_zbtitle(keys)
        for num in nums:
            self.assertIn(keys,num)


    @classmethod
    def tearDownClass(cls):
        pass
 #       cls.driver.quit()







if __name__ == '__main__':
    unittest.main(verbosity=2)  #测试结果会显示详细信息
