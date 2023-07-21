# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 12.使用property返回对应数据.py
@time: 2023/6/21 下午9:21
"""


class Page:
    def __init__(self, current_page):
        # 用户请求的页码
        self.current_page = current_page
        # 每页默认返回的数据个数
        self.page_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.page_items
        return val

    @property
    def end(self):
        val = self.current_page * self.page_items
        return val


p = Page(1)
print(p.start)
print(p.end)

