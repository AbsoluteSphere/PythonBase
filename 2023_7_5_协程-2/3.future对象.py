# -*- coding: utf-8 -*-
# @Time    : 2023/7/5 8:54 下午
# @Author  : 顾安
# @File    : 3.future对象.py
# @Software: PyCharm


# 让future获取不到返回值使await堵塞
import asyncio


async def main():
    loop = asyncio.get_running_loop()  # 获取一个正在运行的事件循环
    fut = loop.create_future()  # 只是创建了一个对象并没有绑定任务
    fut.set_result('模拟返回值...')  # 一旦设置了返回值 则await解除堵塞
    await fut


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

"""
await 解堵塞的前提是future对象有返回值
await 获取到返回值之后 future的对象状态转为完成
"""

