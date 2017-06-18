#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-16 12:55:16
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

import urllib, urllib2
import re, thread, time

# 糗事百科爬虫
class QSBK(object):

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
        # 初始化headers
        self.headers = {'User-Agent': self.user_agent}
        # 存放段子的变量，一个元素保存一页
        self.stories = []
        # 继续标记
        self.enable = False

    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url, headers = self.headers)
            response = urllib2.urlopen(request)
            pageContent = response.read().decode('utf-8')
            return pageContent
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print u'连接糗事百科失败，错误原因：', e.reason
                return None

    def getPageItems(self, pageIndex):
        pageContent = self.getPage(pageIndex)
        if not pageContent:
            print '页面加载失败'
            return None

        regex = '<div.*?author.*?<a.*?<h2>(.*?)</h2>.*?<div.*?content.*?<span>(.*?)</span>.*?<span.*?stats-vote.*?><i.*?number.*?>(.*?)</i>(.*?)</span>.*?<span.*?stats-comments.*?<i.*?number.*?>(.*?)</i>(.*?)</a>'
        pattern = re.compile(regex, re.S)
        items = re.findall(pattern, pageContent)

        pageStories = []
        for item in items:
            oneStory = []
            replaceBR = re.compile('<br/>')
            text = re.sub(replaceBR, '\n', item[1])
            oneStory.append(item[0])
            oneStory.append(text)

            oneStory.append(item[2] if re.search(u'好笑', item[3]) else '0')
            oneStory.append(item[4] if re.search(u'评论', item[5]) else '0')

            pageStories.append(oneStory)

        return pageStories

    # 加载并提取页面的内容，加入到列表中
    def loadPage(self):
        # 如果当前未看的页数少于2页，则加载新一页
        if self.enable == True:
            if len(self.stories) < 2:
                # 获取新一页
                pageStories = self.getPageItems(self.pageIndex)
                # 将改业的段子存放到全局list中
                if pageStories:
                    self.stories.append(pageStories)
                    # 获取完之后页码索引+1，表示下次读取的下一页
                    self.pageIndex += 1

    # 调用该方法，每次敲回车打印输出一个段子
    def getOneStory(self, pageStories, page):
        # 遍历一页的段子
        for story in pageStories:
            # 等待用户输入
            input = raw_input()
            # 每当输入回车一次，判断是否加载新页面
            self.loadPage()
            # 如果输入 Q 则程序结束
            if input == "Q":
                self.enable = False
                return 

            print u'第%d页\t发布者：%s\n%s\n\t点赞数：%s\t评论数：%s' % (page, story[0], story[1], story[2], story[3])

    # 开始方法
    def start(self):
        print u'正在读取糗事百科，按回车查看新段子，Q退出:'
        # 使变量为 True，程序可以正常运行
        self.enable = True
        # 先加载一页内容
        self.loadPage()
        # 局部变量，控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                # 从全局list中获取一页的段子
                pageStories = self.stories[0]
                # 当前读到的页数+1
                nowPage += 1
                # 将全局list中第一个元素删除
                del self.stories[0]
                # 输出段子
                self.getOneStory(pageStories, nowPage)

spider = QSBK()
spider.start()

