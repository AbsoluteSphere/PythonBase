# -*- coding: utf-8 -*-
# @Time    : 2023/7/5 8:12 下午
# @Author  : 顾安
# @File    : 1.task任务的批量提交.py
# @Software: PyCharm


import asyncio


async def work():
    print('任务启动...')
    await asyncio.sleep(2)
    return '模拟一个返回值'


# 创建task对象
async def main():
    tasks = [asyncio.create_task(work()) for _ in range(2)]

    # wait可以接收一个迭代对象并将迭代对象中的元素提交给时间循环 并且可以获取被提交的任务的运行状态
    done, pending = await asyncio.wait(tasks, timeout=3)
    print(done)  # 是一个集合
    for item in done:  # 在done变量中的对象都是已经完成任务的对象
        print(item.result())
    print('pending:', pending)  # 接收的是未完成和正在执行的任务


# async def main():
#     tasks = [asyncio.create_task(work()) for _ in range(2)]
#     gather不能接收迭代对象,*就是开包
#     result_list = await asyncio.gather(*tasks)
#     print(result_list)


# async def main():
#     tasks = [asyncio.create_task(work()) for _ in range(2)]
#
#     for item in asyncio.as_completed(tasks):
#         # as_completed是一个生成器
#         # 在for循环的时候生成器会返回一个对象 future
#         # 当前as_completed获取返回值是异步的
#         res = await item
#         print(res)


asyncio.run(main())

