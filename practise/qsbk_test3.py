#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-17 11:07:55
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.csdn.net/PatrickZheng
# @Version : $Id$

import urllib, urllib2
import re

page = 1

url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
headers = {'User-Agent': user_agent}

try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')

# 版本二，输出：作者、文字内容、图片链接、点赞数、评论数
    regex = '<div.*?author.*?<a.*?<h2>(.*?)</h2>.*?<div.*?thumb.*?<img src="(.*?)".*?<div.*?content.*?<span>(.*?)</span>.*?<span.*?stats-vote.*?><i.*?number.*?>(.*?)</i>(.*?)</span>.*?<span.*?stats-comments.*?<i.*?number.*?>(.*?)</i>(.*?)</a>'

    pattern = re.compile(regex ,re.S)

#1）.*? 是一个固定的搭配，.和*代表可以匹配任意无限多个字符，加上？表示使用非贪婪模式进行匹配，也就是我们会尽可能短地做匹配，以后我们还会大量用到 .*? 的搭配。
#2）(.*?)代表一个分组，在这个正则表达式中我们匹配了五个分组，在后面的遍历item中，item[0]就代表第一个(.*?)所指代的内容，item[1]就代表第二个(.*?)所指代的内容，以此类推。
#3）re.S 标志代表在匹配时为点任意匹配模式，点 . 也可以代表换行符。

    items = re.findall(pattern, content)
    for item in items:
        great = re.search(u'好笑', item[4])
        comment = re.search(u'评论', item[6])
        print '作者：', item[0]
        print '内容：', item[2]
        print 'link: ', item[1]
        if great:
            print '点赞数：', item[3]
        if comment:
            print '评论数：', item[5]
        print '---------------------------------'
except urllib2.HTTPError, e:
    if hasattr(e, 'code'):
        print e.code
except urllib2.URLError, e:
    if hasattr(e, 'reason'):
        print e.reason

