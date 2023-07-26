# -*- coding: utf-8 -*-
# @Time    : 2023/7/17 下午10:24
# @Author  : 顾安
# @File    : 11.获取当前仓库中所有的key.py
# @Software: PyCharm


from redis import Redis


redis_client = Redis()
res = redis_client.keys()
print(res)
