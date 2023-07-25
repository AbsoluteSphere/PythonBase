# -*- coding: utf-8 -*-
# @Time    : 2023/7/3 9:13 下午
# @Author  : 顾安
# @File    : 6.快速上手.py
# @Software: PyCharm


import asyncio


# 协程函数能不能单独运行?
async def work_1():
    print(1)


async def work_2():
    print(2)


"""
1 - 3.6版本运行协程对象
2 - 3.7以上版本运行协程对象
"""

# 3.6
# loop = asyncio.get_event_loop()
# loop.run_until_complete(work())

# 3.7 - 不需要自己创建事件循环
work_list = [
    work_1(),
    work_2()
]

asyncio.run(asyncio.wait(work_list))
