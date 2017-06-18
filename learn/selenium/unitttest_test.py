#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-18 15:58:41
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get('http://www.python.org')
        self.assertIn('Python', driver.title)
        elem = driver.find_element_by_name('q')
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)
        assert 'No results found.' not in driver.page_source
        
        elem2 = driver.find_element_by_name('q') 
        # 由于 elem已经往输入框输入了 pycon，需要调用clear才会清除内容
        elem2.clear()
        elem2.send_keys('next')
        elem2.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
