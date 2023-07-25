# -*- coding: utf-8 -*-
# @Time    : 2023/7/3 8:43 下午
# @Author  : 顾安
# @File    : 5.事件循环的创建.py
# @Software: PyCharm


"""
python3.7以上版本中不需要我们自己手动创建事件循环
    在代码底层自动帮助我们创建

使用python3.6的语法创建一个事件循环
"""

import asyncio


async def work_1():
    for _ in range(5):
        print('协程任务 - 1')
        await asyncio.sleep(1)


async def work_2():
    for _ in range(5):
        print('协程任务 - 2')
        await asyncio.sleep(1)


loop = asyncio.get_event_loop()  # 创建一个事件循环

# 当前列表中存储的是协程对象
coroutines = [
    work_1(),
    work_2()
]

done, pending = loop.run_until_complete(asyncio.wait(coroutines))

for item in done:
    print(type(item))



"""
1.事件循环如何创建 - get_event_loop
2.如何去运行事件循环 - run_until_complete
"""