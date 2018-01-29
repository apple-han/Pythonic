# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/24 19:29'

# (1) 要避免劣化代码

'''
    与优化代码对应，劣化代码就是一开始写出来就是不合理的代码，
    比如不合适的变量命名，通常有以下几个值得注意的地方
    
    1) 避免只用大小写来区分不同的对象。如a是一个数值类型变量，
       A是String类型，虽然在编码过程中很容易区分二者的含义，
       但这么做毫无益处
    2) 避免使用容易引起混淆的名称
'''
# 下面的两个示例中二比一更好

# (一)
def funA(list,num):
    for element in list:
        if num==element:
            return True
        else:
            pass

# (二)
def find_num(searchList,num):
    for ListValue in searchList:
        if num==ListValue:
            return True
        else:
            pass

# 3) 不要害怕过长的变量名，下面的示例中person_info比pi的可读性更强
person_list = {'name': '__apple','IDCard': '320322'}

#(2) 深入理解Python有助于编写Pythonic代码
'''
    1,熟练掌握Python带给我们所有的特性
    2,学习Python的新特性 比如早年的dict.has_key()被in代替了
    3，深入学习业界公认的Pythonic的代码，比如Flask，requests
'''


# 检查代码是否满足PEP8规范

#pip install -U pep8

'''
    其实完全放弃’自我风格‘还是非常难的，要突破这种瓶颈，完成
    自我蜕变，要付出很多的精力去学习，可以多来我的github上面
    学习，haha。
'''
