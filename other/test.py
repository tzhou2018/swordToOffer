# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/1/15 16:48
desc:
'''


def jumpFloor(number):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        return jumpFloor(number - 1) + jumpFloor(number - 2)
