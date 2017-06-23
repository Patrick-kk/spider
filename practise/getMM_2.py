#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-18 21:29:56
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.csdn.net/PatrickZheng
# @Version : $Id$

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup

import requests, urllib2
import os.path

# 有时候网站服务器会拒绝响应
while True:
    # 设置 Headers
    # https://www.zhihu.com/question/35547395
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (user_agent)
    driver = webdriver.PhantomJS(executable_path='D:\workplace\spider\phantomjs-2.1.1-windows\phantomjs.exe', desired_capabilities=dcap)
    driver.get('https://www.taobao.com/markets/mm/mmku')

    soup = BeautifulSoup(driver.page_source, 'lxml')

    # 每个MM的展示是放在 属性class=cons_li的div中
    cons_li_list = soup.select('.cons_li')
    lenOfList = len(cons_li_list)
    print lenOfList

    if lenOfList == 0:
        continue

    for cons_li in cons_li_list:
        name = cons_li.select('.item_name')[0].get_text().strip('\n')
        print name

        img = cons_li.select('.item_img img')[0]
        img_src = img.get('src')
        if img_src is None:
            img_src = img.get('data-ks-lazyload')
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

    driver.close()
    print 'done.'
    break
