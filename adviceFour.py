# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/25 16:54'

######################
# 在代码适当的增加注释  #
#####################

'''
    注释:
        Python中有三种形式的代码注释：
            1，块注释
            2，行注释
                使用行注释或者块注释仅仅注释那些复杂的操作，算法，还有一些
                还有一些别人难以理解的技巧或者不够一目了然的代码如下面的例子
                (1-2)-1,两种注释的方法显然第一种比较好，
                给函数做一些注释(1-2)-2
            3，文档注释（docstring）
               推荐在文档的头部添加copyright申明，模块描述
'''

# (1-2)-1
x = 5
x = x+1      # increace x by 1

x = x+1 # increace x by 1

# (1-2)-2
def FunName(parameter1, parameter2):
    '''
    描述这个函数是做什么的
    :param parameter1:参数的作用
    :param parameter2:
    :return: 返回的值以及对应的类型
    '''
    pass