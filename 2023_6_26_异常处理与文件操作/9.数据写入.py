# -*- coding: utf-8 -*-

"""
@author: 顾安
@software: PyCharm
@file: 9.数据写入.py
@time: 2023/6/26 下午9:16
"""


file_name = '测试文件.txt'  # 后缀名一定要加

# file_obj = open(file_name, mode='w')  # 更改文件打开方式
# file_obj.write('双双, 过来请你吃猪蹄～ 我请客')


file_obj = open(file_name, mode='a')
file_obj.write('\n下午一起去游泳...')


# 关闭文件对象
file_obj.close()




