# -*- coding: utf-8 -*-
# @Time    : 2023/7/3 10:08 下午
# @Author  : 顾安
# @File    : 9.task对象-3.6版本.py
# @Software: PyCharm


"""
task对象是用于任务并发的
"""

import asyncio


async def other(name, address):
    print('other任务被执行...')
    await asyncio.sleep(2)
    print('other任务结束...')
    return f'{name}, {address}'


async def main(loop=None):
    # 将other任务手动打包成task对象
    # python3.6的打包方式
    # 当前task任务打包提交是不耗时的
    task_1 = loop.create_task(other('安娜', '长沙'))
    task_2 = loop.create_task(other('双双', '南京'))

    response_1 = await task_1
    response_2 = await task_2

    print(response_1, response_2)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))






