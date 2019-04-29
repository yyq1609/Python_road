#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1.计算任意一个文件夹的大小（考虑绝对路径的问题）
    基础需求
        这个文件夹中只有文件
    进阶需求
        这个文件夹中可能有文件夹，并且文件夹中还可能有文件夹...不知道有多少层
"""
import os
path_dir = os.path.dirname(os.path.dirname(__file__))
total = os.path.getsize(path_dir)


def dir_count(path):
    global total
    for i in os.listdir(path):
        path_i = os.path.join(path, i)
        print(path_i)
        if os.path.isfile(path_i):
            total += os.path.getsize(path_i)
            continue
        total += os.path.getsize(path_i)
        dir_count(path_i)


if __name__ == '__main__':
    dir_count(path_dir)
    print(total)




