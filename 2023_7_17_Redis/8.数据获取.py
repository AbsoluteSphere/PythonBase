# -*- coding: utf-8 -*-
# @Time    : 2023/7/17 下午10:19
# @Author  : 顾安
# @File    : 8.数据获取.py
# @Software: PyCharm


from redis import Redis


redis_client = Redis()
data = redis_client.get('name')
print(data.decode('utf-8'))
