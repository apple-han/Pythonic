# -*- coding: utf-8 -*-
__author__ = 'Apple'

########################################
#      i+=1 不等于++i                  #
######################################

'''
    对于对Python语言的每个细节了解得不是那么清楚，而恰好又有其他语言
    背景的开发人员，很有可能写出1-21所示的代码，对应这个结果，原因如下：
        因为Python解释器会将++i操作解释为+(+1),其中+表示正数符号。对
        于--1操作也是类似的，因此你需要明白++i在Python中语法上是合法的，
        但并不是我们理解的通常意义上的自增操作
'''

# 1-21
i = 0
mylist = [1,2,3,4,5]
while i < len(mylist):
    print(mylist[i]) # 这个结果是无限制的输出1
    ++i