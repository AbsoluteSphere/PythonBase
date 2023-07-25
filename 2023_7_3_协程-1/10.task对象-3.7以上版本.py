# -*- coding: utf-8 -*-
# @Time    : 2023/7/3 10:19 下午
# @Author  : 顾安
# @File    : 10.task对象-3.7以上版本.py
# @Software: PyCharm


import asyncio


async def other(name, address):
    print('other任务被执行...')
    await asyncio.sleep(2)
    print('other任务结束...')
    return f'{name}, {address}'


# 当前列表中调用的create_task是基于事件循环来创建task的 但是在创建task之前时间循环并不存在
# 大家切记通过asyncio创建task的时候不要写在协程函数外
# tasks = [
#         other('安娜', '长沙'),
#         other('双双', '南京')
# ]


async def main():
    # 将other任务手动打包成task对象
    # python3.6的打包方式
    # 当前task任务打包提交是不耗时的
    # asyncio.create_task: 会自动获取当前存在的事件循环
    task_1 = asyncio.create_task(other('安娜', '长沙'))  # 会进行代码预读
    task_2 = asyncio.create_task(other('双双', '南京'))

    response_1 = await task_1
    response_2 = await task_2
    #
    print(response_1, response_2)

    # done, pending = await asyncio.wait(tasks)
    # for item in done:
    #     print(item.result())


asyncio.run(main())
