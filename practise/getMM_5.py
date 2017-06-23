#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-18 22:21:15
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.csdn.net/PatrickZheng
# @Version : $Id$


from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup

import requests, urllib2
import os.path
import time
import logging

executable_path = 'D:\workplace\spider\phantomjs-2.1.1-windows\phantomjs.exe'

class TaobaoMM(object):

    def __init__(self, url):
        logging.basicConfig(level=logging.INFO,
                format='%(asctime)s [%(levelname)s] %(message)s',
                filename='mm.log',
                filemode='a')

        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
        # 设置 Headers
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (self.user_agent)
        self.driver = webdriver.PhantomJS(executable_path=executable_path, desired_capabilities=dcap)
        self.driver.get(url)
        self.selections = None
        
        logging.info(url+u' 读取完成')

    #创建新目录
    def mkdir(self, path):
        path = path.strip()
        # 判断路径是否存在
        isExists = os.path.exists(path)
        if not isExists:
            # 如果不存在则创建目录
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            return False

    def saveImages(self, path):
        driver = self.driver
        # 获取总共的页数
        pages = int(driver.find_element_by_xpath('//div[@class="paginations"]/span[@class="skip-wrap"]/em').text)
        logging.info(u'====== 共有 %d 页 =====' % pages)

        for i in range(1, pages+1):
            soup = BeautifulSoup(driver.page_source, 'lxml')
            logging.info((u'正在处理第 %d 页...' % i))
            # 每个MM的展示是放在 属性class=cons_li的div中
            cons_li_list = soup.select('.cons_li')
            lenOfList = len(cons_li_list)
            logging.debug(lenOfList)

            for cons_li in cons_li_list:
                name = cons_li.select('.item_name')[0].get_text().strip('\n')
                logging.info(u'昵称：'+name)

                img_src = cons_li.select('.item_img img')[0].get('src')
                if img_src is None:
                    img_src = cons_li.select('.item_img img')[0].get('data-ks-lazyload')
                logging.info(u'照片链接：'+img_src)

                filename = name + os.path.splitext(img_src)[1]
                with open(path+'/'+filename, 'wb') as f:
                    try:
                        headers = {'User-Agent': self.user_agent}
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
                    except urllib2.URLError, e:  # 有可能图片链接有问题
                        if hasattr(e, 'reason'):
                            logging.error(e.reason)

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

    def getSelection(self):
        self.selections = self.driver.find_elements_by_xpath('//div[@class="listing_tab"]/li')
        output = '请选择(0:所有 '
        for i in range(0, len(self.selections)):
            output += str(i+1) + ':' + self.selections[i].text.encode('utf-8') + ' '

        output += ')：'
        return output

    def start(self, select):
        try:
            selections = self.selections
            if select == '0':
                for selection in selections:
                    logging.info(u'开始进行 %s 图片下载' % selection.text)
                    path = './'+selection.text
                    self.mkdir(path)
                    selection.click()
                    time.sleep(2)
                    self.saveImages(path)

            elif int(select) <= len(selections) :
                selection = selections[int(select)-1]
                logging.info(u'开始进行 %s 图片下载' % selection.text)
                path = './'+selection.text
                self.mkdir(path)
                selection.click()
                time.sleep(2)
                self.saveImages(path)

            else:
                logging.info(u'选择有误')
        except Exception, e:
            logging.exception(e)
        finally:
            self.driver.quit()

mm = TaobaoMM('https://www.taobao.com/markets/mm/mmku')
select = raw_input(mm.getSelection())
start = time.time()
mm.start(select)
logging.info((u'共耗时 %.02f 秒' % (time.time()-start)))
