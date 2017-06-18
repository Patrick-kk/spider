#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-17 15:32:58
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.sina.com.cn/kkpatrick
# @Version : $Id$

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')

# 还可以用本地HTML文件来创建
# soup = BeautifulSoup(oepn('index.html'))

print soup.html.find_all('a')

print soup.html.find('a')
