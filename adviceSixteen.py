# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/2/6 13:53'

##############################
#    分清==与is的适应场景      #
############################

'''
    在判断两个字符串是否相等的时候，混用is和==是很多的初学者犯的错误
    造成的结果是程序在不同的情况下表现不一。来看一些列子 如16-1,在命
    令行会有一些不同的情况16-2,出现的原因我在下面做了注释。
'''

# 16-1
# a = 'Hi'
# b = 'Hi'
# if a is b:
#     print(True) # True
# if a == b:
#     print(True) # True

a1 = "I am long string"
b1 = 'I am long string'

a = a1 is b1

print(id(a1))

print(id(b1))

if (a1 is b1):
    print(True) # True
else:
    print(False)

if a1 == b1:
    print(True) # True

'''
    >>> a = 'I am long string'
    >>> b = 'I am long string'
    >>> a is b
    >>> False
'''

'''
    intern机制处理空格一个单词的复用机会大，所以创建一次，有空格创建多次，
    但是字符串长度大于20，就不是创建一次了。

'''
'''
    终端是每次执行一次，所以每次的大整数都重新创建，而在pycharm中，
    每次运行是所有代码都加载都内存中，属于一个整体，所以
    这个时候会有一个大整数对象池，即处于一个代码块的大整数是同一个对象。
'''

'''
    综上所述->在判断对象是否相等的时候，最好要用 == 
'''
