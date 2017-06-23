#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-18 22:32:26
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.csdn.net/PatrickZheng
# @Version : $Id$

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup

import requests, urllib2
import os.path
import time

# 有时候网站服务器会拒绝响应

# 设置 Headers
# https://www.zhihu.com/question/35547395
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (user_agent)
driver = webdriver.PhantomJS(executable_path='D:\workplace\spider\phantomjs-2.1.1-windows\phantomjs.exe', desired_capabilities=dcap)
driver.get('https://www.taobao.com/markets/mm/mmku')

#soup = BeautifulSoup(driver.page_source, 'lxml')

# 获取总共的页数
#pages = int(soup.select('.paginations span[class="skip-wrap"] em')[0].get_text())
pages = int(driver.find_element_by_xpath('//div[@class="paginations"]/span[@class="skip-wrap"]/em').text)
print 'Total pages: %d' % pages

for i in range(1, 3):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    print '第 %d 页：\n' % i
    # 每个MM的展示是放在 属性class=cons_li的div中
    cons_li_list = soup.select('.cons_li')
    lenOfList = len(cons_li_list)
    print lenOfList

    for cons_li in cons_li_list:
        name = cons_li.select('.item_name')[0].get_text().strip('\n')
        print name

        img_src = cons_li.select('.item_img img')[0].get('src')
        if img_src is None:
            img_src = cons_li.select('.item_img img')[0].get('data-ks-lazyload')
        print img_src

        filename = name + os.path.splitext(img_src)[1]
        with open(filename, 'wb') as f:
            headers = {'User-Agent': user_agent}
            # urllib.urlopen 好像不支持添加 headers
            # 换用 requests 库
            # https://segmentfault.com/q/1010000007024942?_ea=1212676

            '''
            ir = requests.get(img_src if img_src.startswith('http') else 'http:'+img_src, headers=headers, stream=True)
            if ir.status_code == 200:
                f.write(ir.content)
            '''

            # urllib2 可以添加 headers
            # http://www.jianshu.com/p/6094ff96536d
            request = urllib2.Request(img_src if img_src.startswith('http') else 'http:'+img_src, None, headers)
            response = urllib2.urlopen(request)
            f.write(response.read())

    # 找到页码输入框
    pageInput = driver.find_element_by_xpath('//input[@aria-label="页码输入框"]')
    pageInput.clear()
    pageInput.send_keys(str(i+1))

    # 找到“确定”按钮，并点击
    ok_button = driver.find_element_by_xpath('//button[@aria-label="确定跳转"]')
    ok_button.click()

    # 睡2秒让网页加载完再去读它的html代码
    # http://www.tuicool.com/articles/22eY7vQ
    time.sleep(2)

# http://www.jianshu.com/p/9d408e21dc3a
# 之前是使用 driver.close()，但这个不确保关闭 phantomjs.exe
# 会导致一直占用着内存
driver.quit()
print 'done.'

