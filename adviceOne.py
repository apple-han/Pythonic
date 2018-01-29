# -*- coding: utf-8 -*-
__author__ = '__apple'

# (1) 理解pythonic的概念

############################
#  << The Zen of Python >> #
############################

def quicksort(array):
    less = []; greater = []
    if len(array) <= 1:
        return array
    pivot = array.pop()
    for x in array:
        if x <= pivot: less.append(x)
        else:greater.append(x)
    return quicksort(less)+[pivot]+quicksort(greater)

quicksort([3,3213,234,2344,43,2,4,3,2,24,45]) # [2, 2, 3, 3, 4, 24, 43, 45, 234, 2344, 3213]

# (2) 代码风格

# C语言中交换变量

###########################
#  int a=1, b=2;         #
#  int tmp = a'         #
#  a = b;              #
#  b = tmp            #
######################

# python中交换变量、

a = 1;b = 2
a, b = b, a

# 遍历一个容器的时候，其他的语言是这么做的

################################
# length = len(alist)         #
# i = 0                      #
# while i < length:         #
#     do_sth_with(alist[i])#
#     i += 1              #
##########################

# python的代码如下

alist = [1,2,43,4,3,3,2]

def do_sth_with(i):
    print(i)

for i in alist:
    do_sth_with(i)

# 如果你需要安全的关闭文件扫描使用with是一个不错的选择

import os

PATH = (os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))+
        os.sep+'one_text.txt')

with open(PATH, 'r') as f:
    f.readline()

'''
    总结：
        通过上述的代码的对比，能让大家清晰地认识到Pythonic的一个要求，
        就是对Python语法本身的充分发挥，写出来的代码带着Python味儿，
        而不是看着像C语言代码，或者Java代码。
        应当追求的是充分利用Python语法，但不应该过分地使用奇技淫巧，
        比如利用Python的Slice语法，如下
'''

a = [1,2,3,4]
c = 'abcdef'
print(a[::-1])
print(c[::-1])

'''
    如果不是同样追求每一个语法细节的'老鸟'，上面这段代码的作用恐怕不能一眼就看出来。
    实际上，这个时候更好地体现Pythonic的代码是充分利用Python库里reversed()函数
    的代码。
'''

print(list[reversed(a)])
print(list[reversed(c)])

# (3) 标准库

'''
    写Pythonic程序需要对标准库有充分的理解，特别是内置函数和内置数据类型。
    比如，对于字符串格式化，一般这么写:
'''
print('Hello %s!' % ('Tom',))

'''
    其实%s是非常影响可读性的，因为数量多了以后，很难清楚哪一个占位符对应哪一个实参。
    所以对应的Pythonic代码是这样的：
'''
print('Hello %(name)s!' % {'name': 'Tom'})

# 更具Pythonic的写法如下
print('{greet} from {language}.'.format(greet = 'Hello World', language = 'Python'))

# (4) Pythonic的库或框架

# 现在业内通常认为Flask这个框架比较Pythonic的，它的一个Hello world级别的用例如下：
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello world!"
if __name__ == "__main__":
    app.run()

'''
    事实上这些年来优秀的Python代码的特性也在不断演化。
    比如现在像generators之类的特性尤为Pythonic。
    这里有一些库或者框架跟随了一下的潮流
    . 包和模块的命名采用小写，单数形式，而且短小
    . 包通过作用命名空间，如只包含空的__init__,py文件。    
'''






