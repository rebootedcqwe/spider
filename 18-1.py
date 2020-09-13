#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version  : Python 3.7
class Person3:   # 创建类
    def __init__(selfa, name1, age1): #__init__()方法称为类的构造方法
        selfa.name2 = name1
        selfa.age2 = age1
 
    def detailaa(selfb): #通过self调用被封装的内容
        print (selfb.name2)
        print (selfb.age2)

obj17 = Person3('oliver', 77)
obj17.detailaa()  # Python将obj1传给self参数，即：obj1.detail(obj1)，此时内部self＝obj1
