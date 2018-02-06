# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/31 18:24'

##############################
#    使用enumerate()         #
############################

'''
    基本上所有的项目都存在对序列进行迭代并获取序列中的元素进行处理的情形，
    相信很多人可以一口气写出N种方法，如下所示
'''

# 15-1
# li = ['a','b','c','d','e']
# index = 0
# for i in li:
#     print("index:",index,"element:",i)
#     index += 1
#
# # 15-2
# for i in range(len(li)):
#     print("index:",index,"element:",li[index])
#     index+=1
#
# # 15-3
# while index < len(li):
#     print("index:",index,"element:",li[index])
#     index += 1
#
# # 15-4
# # 使用zip的方式
# for i, e in zip(range(len(li)), li):
#     print("index:",i,"element:",e)
#
#
# # 15-5
# for i,e in enumerate(li):
#     print("index:",i,"element:",e)

'''
    这里推荐低五种方式代码简洁，可读性强，enumerate也可以是一个迭代器如下
'''
li = ['a','b','c','d','e']
print(enumerate(li)) # <enumerate object at 0x021D0508>
e = enumerate(li)
print(e.__next__())
print(e.__next__())
#(0, 'a')
#(1, 'b')

