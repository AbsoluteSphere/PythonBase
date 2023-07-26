# -*- coding: utf-8 -*-
# @Time    : 2023/7/17 下午10:21
# @Author  : 顾安
# @File    : 9.修改数据.py
# @Software: PyCharm


from redis import Redis


redis_client = Redis()

redis_client.set('name', '双双')
res = redis_client.get('name')
print(res.decode())

