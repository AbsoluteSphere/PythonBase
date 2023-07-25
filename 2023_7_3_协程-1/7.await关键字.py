# -*- coding: utf-8 -*-
# @Time    : 2023/7/3 9:20 下午
# @Author  : 顾安
# @File    : 7.await关键字.py
# @Software: PyCharm


"""
await是用于等待的关键字
    事件循环可以自动进行任务切换
        切换的根据是当前这个任务是否是耗时任务
            await去判断
"""

import asyncio


async def other():
    print('other任务启动...')
    # 模拟一个耗时任务
    await asyncio.sleep(5)
    print('other任务完成...')
    # 当前任务有返回值
    return '模拟返回的数据...'


async def func():
    print('当前正在执行协程函数内部代码...')
    response = await other()  # 卡住了 5秒钟: await的本质其实就是提交任务并等待任务的返回值
    print(f'返回值的内容为: {response}')

# 3.6
# 1. 创建事件循环
loop = asyncio.get_event_loop()
loop.run_until_complete(func())


"""
    await 可以将任务进行提交事件循环中
    await 只能提交可等待对象 - [coro, task, future]
    await 可以接收一个任务的返回值 - 如果没有接收到返回值一直等待
"""



