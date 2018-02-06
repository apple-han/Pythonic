# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/31 17:57'

##############################
#    警惕exal()的安全漏洞     #
############################

'''
    如果你了解js或者PHP等，那么你对eval()肯定有所了解，
    eval()也很简单如14-1
'''
# 14-1
print(eval("1+1==2")) # True

print(eval("'A'+'B'")) # AB

print(eval("1+2"))    # 3

# 那么我们来看一下eval有什么漏洞呢？看14-2

import sys
from math import *

def ExpCalcBot(string):
    try:
        print('Your answer is',eval(string))
    except NameError:
        print('The expression you enter is not valid')
print("Hi,I'm apple")
inputstr = ''
while 1:
    print('Please enter a number or operation.Enter c to complete.:')
    inputstr = input()
    if inputstr == str('e'):
        sys.exit()
    elif repr(inputstr) != repr(''):
        ExpCalcBot(inputstr)
        inputstr = ''

# 如果是正常的用户当然不会有问题，比如比输入1+1结果就是2，
# 但是如果是有人故意要钻空子，输入了__import__("os").system("dir")
# 就出现了下面这种情况，把我们所有的文件都取出来了

# 2018/01/29  14:23             1,770 adviceEleven.py
# 2018/01/25  20:11             3,655 adviceFive.py
# 2018/01/25  17:09             1,062 adviceFour.py
# 2018/01/31  18:22             1,114 adviceFourteenth.py
# 2018/01/24  18:11             3,543 adviceOne.py
# 2018/01/29  13:46             1,437 adviceSeven.py
# 2018/01/26  17:03             3,352 adviceSix.py
# 2018/01/31  17:59               475 adviceThirteenth.py
# 2018/01/25  16:56             2,190 adviceThree.py
# 2018/01/31  14:26             2,700 adviceTwelve.py