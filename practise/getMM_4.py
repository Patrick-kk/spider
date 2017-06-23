#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-19 11:32:55
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.csdn.net/PatrickZheng
# @Version : $Id$

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup

import requests, urllib2
import os.path
import time


#创建新目录
def mkdir(path):
    path = path.strip()
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False

# 设置 Headers
# https://www.zhihu.com/question/35547395
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (user_agent)
driver = webdriver.PhantomJS(executable_path='D:\workplace\spider\phantomjs-2.1.1-windows\phantomjs.exe', desired_capabilities=dcap)
driver.get('https://www.taobao.com/markets/mm/mmku')

selections = driver.find_elements_by_xpath('//div[@class="listing_tab"]/li')

output = '请选择(0:所有 '

for i in range(0, len(selections)):
    output += str(i+1) + ':' + selections[i].text.encode('utf-8') + ' '

output += ')：'

user_select = raw_input(output)

print user_select


for selection in selections:
    pages = int(driver.find_element_by_xpath('//div[@class="paginations"]/span[@class="skip-wrap"]/em').text)
    print 'Total pages: %d' % pages

    mkdir('./'+selection.text)

    selection.click()

    time.sleep(2)


# http://www.jianshu.com/p/9d408e21dc3a
# 之前是使用 driver.close()，但这个不确保关闭 phantomjs.exe
# 会导致一直占用着内存
driver.quit()
print 'done.'


