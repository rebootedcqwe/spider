#!/usr/bin/python
# coding: utf-8

import requests
#link = "http://www.santostang.com/"
linkaa = "http://www.163.com/"
headersa = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 

ra = requests.get(linkaa, headers= headersa)
print (ra.text)
