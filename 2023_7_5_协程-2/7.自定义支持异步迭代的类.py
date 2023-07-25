# -*- coding: utf-8 -*-
# @Time    : 2023/7/5 9:26 下午
# @Author  : 顾安
# @File    : 7.自定义支持异步迭代的类.py
# @Software: PyCharm


# 异步迭代器
import asyncio


class MyAsyncIter:
    def __init__(self):
        self.count = 0

    async def iter_num(self):
        await asyncio.sleep(1)
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    # 异步迭代协议
    def __aiter__(self):
        return self

    async def __anext__(self):
        value = await self.iter_num()
        if value is None:
            raise StopAsyncIteration
        return value


async def iter_func():
    async for item in MyAsyncIter():
        print(item)


asyncio.run(iter_func())
