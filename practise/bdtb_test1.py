#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-17 11:58:08
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

import urllib, urllib2
import re

# 处理页面标签
class Tool(object):
    # 去除img
    removeImg = re.compile('<img.*?>')
    # 去除超链接
    removeAddr = re.compile('<a.*?>|</a>')
    # 换行符替换
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 表格制表<td>替换\t
    replaceTD = re.compile('<td>')
    # 段落开头
    replacePara = re.compile('<p.*?>')
    # 换行符替换
    replaceBR = re.compile('<br><br>|<br>')
    # 剔除其他标签
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n  ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        return x.strip()

# 百度贴吧爬虫
class BDTB(object):

    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self, baseURL, see_lz, floorTag='1'):
        self.baseURL = baseURL
        self.see_lz = '?see_lz=' + str(see_lz)
        self.tool = Tool()
        self.file = None
        self.defaultTitle = 'default'
        self.floor = 1
        self.floorTag = floorTag

    # 传入页码，获取该页帖子的代码
    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.see_lz + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print u'连接百度贴吧失败，错误原因：', e.reason
                return None
    # 提取标题
    def getTitle(self, page):
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    # 提取总页码
    def getPageNum(self, page):
        pattern = re.compile('<li class="l_reply_num.*?<span class="red">(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    # 提取正文
    def getContent(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            content = '\n' + self.tool.replace(item) + '\n'
            #contents.append(content.encode('utf-8'))
            # http://blog.csdn.net/mindmb/article/details/7898528
            contents.append(content)
        return contents

    def setFileTitle(self, title):
        if title is None:
            title = self.defaultTitle
        # 使用open()时，这样写open(name.decode('utf-8'), 'w'),这样创建的中文文件名就没有乱码问题了
        # http://www.cnblogs.com/dragonisnotghost/p/4515581.html
        self.file = open((title + '.txt').decode('utf-8'), 'w+')

    def writeData(self, contents):
        for item in contents:
            if self.floorTag == '1':
                floorLine = "\n" + str(self.floor) + u"-----------------------------------------------------------------------------------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1

    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print 'URL已失效，请重试'
            return
        try:
            print '该帖子共有 ' + str(pageNum) + ' 页'
            for i in range(1, int(pageNum)+1):
                print '正在写入第' + str(i) + '页的数据'
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        except IOError, e:
            if hasattr(e, 'message'):
                print '写入异常：' + e.message
        finally:
            self.file.close()
            print '写入完成'

print u'请输入帖子代号'
baseURL = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
seeLZ = raw_input(u'是否只获取楼主发言：(1:是,0:否)\n')
floorTag = raw_input(u'是否写入楼层信息：(1:是,0:否)\n')
bdtb = BDTB(baseURL, seeLZ, floorTag)
bdtb.start()
