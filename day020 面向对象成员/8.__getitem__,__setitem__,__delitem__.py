#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
用于索引操作，如字典。以上分别表示获取、设置、删除数据
"""


class Foo(object):

    def __getitem__(self, key):
        print('__getitem__', key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()

result = obj['k1']      # 自动触发执行 __getitem__
obj['k2'] = 'henry'     # 自动触发执行 __setitem__
del obj['k1']           # 自动触发执行 __delitem__


