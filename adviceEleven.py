# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/29 12:48'

################################
#      理解枚举代替实现的缺陷     #
###############################

'''
    关于枚举的例子大概非季节和星期莫属了，它能够以更接近
    自然语言的方式来表达数据，使得程序的可读性和可维护性
    大大提高。然而，很不幸，也许你习惯了其他语言中的枚举
    类型，但是在Python3.4以前并不提供。但是在PEP354中提
    出了增加枚举的建议，但被拒绝。也是人们利用Python的动
    态性这个特性，想出了枚举的各种替代方式，如11-1,上面这
    个例子可以简化为11-2,我们还可以借助函数实现如11-3,还
    可以使用collects.namedtuple如11-4
'''

# 11-1
class Seasons:
    Spring = 0
    Summer = 1
    Autumn = 2
    Winter = 3

# print(Seasons.Spring)

# 11-2
class Seasons:
    Spring,Summer,Autumn,Winter = range(4)

# 11-3
def enum(*posarg, **keyarg):
    return type("Enum", (object,), dict(zip(posarg,range(len(posarg))), **keyarg))

Seasons = enum("Spring", "Summer", "Autumn","Winter=1")

# print(Seasons.Spring)

# 11-4
from collections import namedtuple
Seasons = namedtuple('Seasons','Spring Summer Autumn Winter')._make(range(4))
print(Seasons.Spring)

# 关于collections的更多使用方法请关注我的github主页

'''
    那么既然有这么多的替代方案，大家还是执着地提出
    要求语言实现枚举呢？显然，这些替代都有不合理的
    地方，例如11-5,很显然这里有重复的也没有报错
'''
# 11-5
print (Seasons._replace(Spring = 2))     # Seasons(Spring=2, Summer=1, Autumn=2, Winter=3)

