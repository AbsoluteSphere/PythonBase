# -*- coding: utf-8 -*-
# @Time    : 2023/7/5 9:35 下午
# @Author  : 顾安
# @File    : 8.绑定回调.py
# @Software: PyCharm


import asyncio


async def work(name, gender):
    print(f'姓名: {name}, 性别: {gender}')
    return f'返回值: {name}, {gender}'


def get_return(task_obj):
    print(f'{task_obj.result()}')


# 创建事件循环
loop = asyncio.get_event_loop()

# 将协程对象转为task对象
task = loop.create_task(work('安娜', '女'))

# 将获取返回值的函数加入到task对象中
task.add_done_callback(get_return)

# 运行任务并获取任务返回值
loop.run_until_complete(task)

