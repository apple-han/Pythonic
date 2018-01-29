# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/24 19:50'

##############################
# 理解Python与C语言不同之处    #
############################

'''
    我们都知道，Python底层是用C实现的，但切记用
    C语言的思维与风格来编写Python代码
'''

# 主要有以下不同
'''
    1) C,C++,Java等语言是用花括号{}来分隔代码段的不同,Python
       中使用严格的代码缩进来分隔代码块，避免缩进带来的困扰的方法
       之一就是养成良好的习惯，统一缩进风格，不要混用Tab和空格
    2) '与'
        C语言中单引号(')与双引号(")有严格的区别,单引号代表一个字符
        它实际对应于编译器所采用的字符集中的一个整数值。例如在ASCII
        码中，'a'与97对应。而双引号则表示字符串，默认以'\0'结尾，但在
        Python中，单引号与双引号没有明显的区别，仅仅在输入字符串内容不
        同时，在使用上存在微小差异。
        
        >>> string1 = "He said, \"Hello\""
        >>> string1
        >>> 'He said, "Hello"'
        >>> string2 = 'He said,"Hello"'
        >>> string2
        >>> 'He said,"Hello"'
    3) 三元操作符
       三元操作符是if...else的简写方法，语法形式为C?X:Y,它表示当条件C
       为True的时候取值X,C为False的时候取值为Y。这种简洁的方法也一直很受
       开发人员的喜爱，但在python2.5之前不支持这种写法，因此有很多人给了
       一些建议，最终在PEP308被接受，
       >>> X=0
       >>> Y=-2
       >>> print X if X<Y else Y
       >>> -2
    4)switch...case
      Python中没有C语言那样的switch...case分支语句，不过这不是什么难事
      Pyhton中有很多替代方案。假设，用C语言实现的switch...case语句如4-1
      用python实现两种替代方案4-2
'''

# 4-1
'''
switch(n){
    case 0:
      print('You Are Right')
}
'''

# 4-2
n = 0
if n==0:
    print('You Are Right')
#4-2-2
def f(x):
    return {
        0:"You Are Right"
    }.get(n,"nothing")