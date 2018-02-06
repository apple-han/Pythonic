##############################
# 不推荐使用type来进行类型的检查#
############################


'''
    作为动态性的强类型语言，Python中的变量在定义的时候，并不会指定具体的类型
    Python解释器会在运行时自动进行类型检查并根据，需要进行隐式类型转换。按照
    Python的理念，为了充分利用其动态语言的特征是不推荐进行类型检查的。如下面
    的函数add()如12-1,在无需对参数进行任何约束的情况下便可以轻松地实现字符串的连接
    数字的加法、列表的合并等多种功能，甚至处理复数都非常灵活。解释器能够根据
    变量类型的不同调用合适的内部方法进行处理，而当a、b类型不同而两者之间又不能
    进行隐式转换的时候，便抛出了TypeError异常
'''

# 12-1
def add(a,b):
    return a+b

# print(add(1,2j))      # (1+2j)
#
# print(add('a', 'b'))  # ab
#
# print(add(1.0,2.3))   # 3.3
#
# print(add([1,2],[2,3])) # [1, 2, 2, 3]
#
# print(add(1,'a'))       # TypeError: unsupported operand type(s) for +: 'int' and 'str'

'''
    不刻意的进行类型检查，而是在出错的情况下通过抛出异常来进行处理，这是
    比较常见的做法，但实际上应用中为了提高程序的健壮性，仍然会面临进行类
    型检查的场景，那么使用什么方法呢？很容易想到的是type()。内建函数
    type(object)用于返回当前对象的类型，如type(1)返回<type 'int'>
    所有的基本类型都可以在type中找到，如types.BooleanType、types.IntType、
    等，那是不是使用type就可以高枕无忧了呢，我们不推荐使用type来进行变量的
    检查，是有原因的，来看几个例子如11-2
'''

# 12-2
import types
class UserInt(int):
    def __init__(self, val=0):
        self._val = int(val)

    def __add__(self, val):
        if isinstance(val, UserInt):
            return UserInt(self._val + val._val)
        return self._val + val

    def __iadd__(self, val):
        raise NotImplementedError("not support operation")

    def __str__(self):
        return str(self._val)

    def __repr__(self):
        return 'Integer(%s)' %self._val

n = UserInt()
print(n) # 0
m = UserInt(2)
print(m) # 2
print(n+m) # 2

print(type(n) is int) # Fasle
'''
    上面n输出False这说明type()函数并不认为n是int类型，但UserInt继承int，
    显然这与判断是不合的，由此可见，基于内建扩展的用户自定义类型，type函数
    并不能准确的返回结果，我们应该尽量的使用isinstance检测
'''
