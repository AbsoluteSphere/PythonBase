# -*- coding: utf-8 -*-
# @Time    : 2023/7/5 9:54 下午
# @Author  : 顾安
# @File    : 9.返回值获取.py
# @Software: PyCharm


import asyncio


async def work():
    print('任务启动...')
    await asyncio.sleep(1)
    return '返回值'


# 创建事件循环
loop = asyncio.get_event_loop()

# 将协程对象转为task对象
task = loop.create_task(work())

# 使用事件循环调度任务
result = loop.run_until_complete(task)
# print(result)

# 使用task对象获取返回值
print(task.result())
