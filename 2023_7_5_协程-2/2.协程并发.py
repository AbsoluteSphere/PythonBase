# -*- coding: utf-8 -*-
# @Time    : 2023/7/5 8:42 下午
# @Author  : 顾安
# @File    : 2.协程并发.py
# @Software: PyCharm

import asyncio


async def work():
    print('协程任务启动...')
    await asyncio.sleep(1)
    return '返回值'


# loop = asyncio.get_event_loop()


async def main():
    # asyncio.create_task: 必须保证时间循环存在才能创建task对象
    tasks = [asyncio.create_task(work()) for _ in range(2)]
    done, pending = await asyncio.wait(tasks)

    for item in done:
        print(item.result())

    # 在main函数中也有一个返回值
    return '这是main函数的返回值'


main_result = asyncio.run(main())
print(main_result)


"""
asyncio语法需要统一
    不要在python3.7的语法中使用3.6的语法
"""