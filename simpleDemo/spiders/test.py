#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/10 下午11:29
# @Author  : 刘心贤
# @File    : test.py
# @Software: PyCharm Community Edition

if __name__ == '__main__':
    a = ['1','2','3']

    b = ['one','two','three']

    for c,d in zip(a,b):
        print '{},{}'.format(c,d)