# -*- coding: utf-8 -*-
# @Time    : 2023/7/17 下午10:22
# @Author  : 顾安
# @File    : 10.删除数据.py
# @Software: PyCharm

from redis import Redis


redis_client = Redis()

res = redis_client.delete('name')
print(res)
