# -*- coding: utf-8 -*-
__author__ = 'Apple'

###############################
#      利用assert语句来发现问题  #
#############################

'''
    断言（arrert）在很多语言中都是存在的，它主要是调试服务，
    能够更加方便的检查程序的异常，或发现不恰当的输入等，其基
    础语言如 assert expression [",", expressions]
    其中计算expression1 的值会返回True或者是False,当值
    为False的时候会引发Assertion,而expression2是可选的
    举个简单的例子1-8
'''

# 1-8
x = 1
y = 2
assert x ==y,'not equals'