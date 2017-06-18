#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-18 16:03:38
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='D:\workplace\spider\phantomjs-2.1.1-windows\phantomjs.exe')
driver.get('http://www.baidu.com/')
driver.find_element_by_id('kw').send_keys(u'搜索一下')
driver.find_element_by_id('su').click()
print driver.current_url
driver.quit()
