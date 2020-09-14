#!/usr/bin/python
# coding: utf-8

import requests
from bs4 import BeautifulSoup     #从bs4这个库中导入BeautifulSoup

linkcc= "http://www.santostang.com/"
headersbb = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 
r55 = requests.get(linkcc, headers= headersbb)

soupf1 = BeautifulSoup(r55.text, "html.parser")      #使用BeautifulSoup解析这段代码
title34 = soupf1.find("h1", class_="post-title").a.text.strip()
print (title34)
