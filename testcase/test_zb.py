import unittest
from selenium import webdriver
import sys
sys.path.append("/Users/maimai/Desktop/UI_selenium_test/normal/")
from zhibo import zhiboPage
from ddt import ddt,data,unpack
import time

@ddt
class TestZhiBo(unittest.TestCase):

    @classmethod  #不需要实例化
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    now_time=str(int(time.time()))
    @data({"fenlei":'.el-select:first-child','fenlei_child':'.el-select-dropdown__item:nth-child(6)','zhibo_title':'直播标题'+now_time,'zhibo_sub':'直播简介',
           'pic_url':"/Users/maimai/Desktop/mamen.png",'zhibo_fwb':'这里是富文本','zhibo_status':'.self-footer>.nb-button-wrapper:nth-child(2)'})
    @unpack
    def test_insertzhibo(self,fenlei,fenlei_child,zhibo_title,zhibo_sub,pic_url,zhibo_fwb,zhibo_status):
        zb = zhiboPage(self.driver)
        zb.insertzhibo(fenlei,fenlei_child,zhibo_title,zhibo_sub,pic_url,zhibo_fwb,zhibo_status)
        text = zb.detailzb()
        print(text)
        self.assertEqual("直播标题",text)

    def test_fabuzhibo(self):
        zb = zhiboPage(self.driver)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity=2)  #测试结果会显示详细信息