#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-06-21 09:51:32
# Project: zhilianzhaopin

from pyspider.libs.base_handler import *

PAGE_START = 1
PAGE_END = 1
DIR_PATH = 'D:/workplace/spider/jobs'

class Handler(BaseHandler):
    crawl_config = {
        'headers':{
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
        }
    }

    def __init__(self):
        self.base_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=深圳&kw=数据&p='
        self.page_num = PAGE_START
        self.total_num = PAGE_END
        self.deal = Deal()
    
    def on_start(self):
        while self.page_num <= self.total_num:
            url = self.base_url + str(self.page_num)
            self.crawl(url, callback=self.index_page)
            self.page_num += 1

    def index_page(self, response):
        for each in response.doc('td.zwmc a').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False)

    def detail_page(self, response):
        job_name = response.doc('h1').text()
        company_name = response.doc('.fl a').text()
        salary = response.doc('.terminalpage-left li:nth-child(1) > strong').text()
        work_place = response.doc('.terminalpage-left li:nth-child(2) > strong').text()
        education = response.doc('.terminalpage-left li:nth-child(5) > strong').text()
        experience = response.doc('.terminalpage-left li:nth-child(6) > strong').text()
        recruit_num = response.doc('.terminalpage-left li:nth-child(7) > strong').text()
        category = response.doc('.terminalpage-left li:nth-child(8) > strong').text()
        description = response.doc('.tab-cont-box > div > p').text()
        work_place_detail = response.doc('.tab-cont-box h2').text()
        
        
        filename = 'all.csv'
        
        self.deal.saveData(job_name+',', filename)
        self.deal.saveData(company_name+',', filename)
        self.deal.saveData(salary+',', filename)
        self.deal.saveData(work_place+',', filename)
        self.deal.saveData(education+',', filename)
        self.deal.saveData(experience+',', filename)
        self.deal.saveData(recruit_num+',', filename)
        self.deal.saveData(category+',', filename)
        self.deal.saveData(work_place_detail+',', filename)
        self.deal.saveData(description+'\r\n', filename)

    
import os
import codecs

class Deal(object):
    def __init__(self):
        self.path = DIR_PATH
        if not self.path.endswith('/'):
            self.path = self.path + '/'
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            
    def saveData(self, content, path):
        f = codecs.open(self.path + path, 'a', 'utf-8')
        f.write(content)
        f.close()