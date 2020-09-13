#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version  : Python 3.7
class Animal12:
    def eat(selfmmss):
        print ("%s 吃 " %selfmmss.name99)
    def drink(self):
        print ("%s 喝 " %self.name99) 
    def shit(self):
        print ("%s 拉 " %self.name99) 
    def pee(selfkk):
        print ("%s 撒 " %selfkk.name99)

class Cat(Animal12): 
    def __init__(self123, name56):
        self123.name99 = name56 
    def cry(self78):
        print ('喵喵叫')

class Dog(Animal12): 
    def __init__(self00, name88):
        self00.name99 = name88
    def cry(self39aa0):
        print ('汪汪叫')
        
c1 = Cat('小白家的小黑猫')
c1.eat()
c1.cry()
 
d1 = Dog('胖子家的小瘦狗')
d1.pee()
