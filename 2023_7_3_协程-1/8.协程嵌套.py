# -*- coding: utf-8 -*-
# @Time    : 2023/7/3 9:41 下午
# @Author  : 顾安
# @File    : 8.协程嵌套.py
# @Software: PyCharm


import asyncio


async def other():
    print('other任务启动...')
    await asyncio.sleep(3)
    print('other任务结束...')
    return '模拟一个任务的返回值'


async def main():
    print('执行main函数任务...')
    # response_1 = await other()
    # response_2 = await other()
    list_obj = [
        other(),
        other()
    ]

    # 如果代码出现警告使用以下语句
    # list_obj = [
    #     asyncio.create_task(other()),
    #     asyncio.create_task(other())
    # ]
    done, pending = await asyncio.wait(list_obj)
    # 在执行任务的过程中可能有些任务没有完成 将没有完成的任务打包给pending - 任务状态

    for item in done:
        print(item.result())


# 3.7版本以上语法
asyncio.run(main())

"""
很像之前所写到的同步代码

    run方法执行了哪些代码:
        1. 自动的帮你创建一个事件循环
        2. run方法是运行事件循环对象的
        
    asyncio.wait
        1. 需要接收一个迭代对象 - 列表 元组 集合...
        2. 将迭代对象中的元素提取出来并打包成task对象 - 3.6 - 3.9
"""