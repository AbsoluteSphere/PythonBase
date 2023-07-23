# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 10.读写行.py
@time: 2023/6/26 下午9:24
"""

file_path = '测试文件.txt'

file_obj = open(file_path)

# result = file_obj.readline()  # 读取文件中的第一行
# print(result)

result = file_obj.readlines()  # 整个文件, 并且将文件数据打包成列表进行返回
print(result)
#
# file_obj.close()

# file_obj = open(file_path, mode='a')
#
# message_list = ['\n你好呀', '\n我是安娜', '\n很高兴认识你']
# file_obj.writelines(message_list)

file_obj.close()
