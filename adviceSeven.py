# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/26 17:23'

###############################
#      将常量集中到一个文件      #
#############################

'''
    Python中存在常量吗？相信很多人的答案都是否定的。实际上
    Python的内建命名空间是支持一小部分常量的，如我们熟悉的
    True,False,None等，只是Python没有提供定义常量的直接
    方式而已。那么，在Python中应该如何使用常量呢？一般来说
    有以下两种方式：
        1) 通过命名规范来告诉使用者字母大写代表常量
        2) 通过自定义的类来实现常量的功能 详情看1-1
    如1-1代码所示，它对应的模块名为_const,使用的时候
    只要:
    >>> import const
    >>> const.COMPANY = "IBM"
    以上的这种方式一旦设置了就不可以更改了，还有最好把所有的
    常量都放到一个文件里面
'''

# 1-1

class _const(object):
    class ConstError(TypeError): pass
    class ConstCaseErroe(ConstError): pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't change const.%s" % name)
        if not name.isupper():
            raise self.ConstCaseErroe('const name "%s" is not all uppercase' % name)
        self.__dict__[name] = value

import sys
sys.modules[__name__]=_const()



