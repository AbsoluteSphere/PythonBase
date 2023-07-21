# -*- coding: utf-8 -*-
# @Time    : 2023/7/19 下午10:16
# @Author  : 顾安
# @File    : 4.python_with_mongo.py
# @Software: PyCharm


from pymongo import MongoClient

# 1.链接mongodb
client = MongoClient(host='localhost', port=27017)

# 2.j进入到指定数据库
collection = client['mongo_data_info']['test_python']

# 3.在不存在的集合中插入数据
# res = collection.insert_one({'name': '安娜', 'age': 20})
# print(res)

# data_list = [{'name': '双双', 'age': 18}, {'name': '顾安', 'age': 20}]
# collection.insert_many(data_list)


# 查询一条数据
# t_1 = collection.find_one({'name': '安娜'})
# print(t_1)

# 查询多条数据
# t_2 = collection.find({'name': '安娜'})
# for item in t_2:
#     print(item)


# 数据更新
# collection.update_one({'name': '顾安'}, {'$set': {'name': '夏洛'}})

# collection.update_many({'name': '安娜'}, {'$set': {'name': '大海'}})

# import time
# collection.insert_one({'object': time.time()})

# collection.delete_many()

collection.drop()



