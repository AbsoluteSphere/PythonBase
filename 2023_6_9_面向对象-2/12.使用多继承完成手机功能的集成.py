# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 12.使用多继承完成手机功能的集成.py
@time: 2023/6/9 下午9:59
"""


class Camera:
    def take_photo(self):
        print('正在拍照...')


class Movie:
    def play_movie(self):
        print('正在看电影...')


class Iphone(Camera, Movie):
    def call(self):
        print('打电话...')


mobile = Iphone()
mobile.call()
mobile.take_photo()
mobile.play_movie()


"""
将多个类中的方法集成到一个类中
"""

