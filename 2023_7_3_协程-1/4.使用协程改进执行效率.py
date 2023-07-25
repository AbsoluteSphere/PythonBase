# -*- coding: utf-8 -*-
# @Time    : 2023/7/3 8:27 下午
# @Author  : 顾安
# @File    : 4.使用协程改进执行效率.py
# @Software: PyCharm


import time
import asyncio


async def func():
    await asyncio.sleep(1)
    print('这是一个协程任务...')


now = lambda: time.time()

start = now()

loop = asyncio.get_event_loop()

tasks = [loop.create_task(func()) for _ in range(5)]
loop.run_until_complete(asyncio.wait(tasks))


print(f'同步程序所花费的时间为: {now() - start}')
