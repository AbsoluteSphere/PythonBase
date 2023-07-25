# -*- coding: utf-8 -*-
# @Time    : 2023/7/5 9:59 下午
# @Author  : 顾安
# @File    : 10.异步上下文管理器.py
# @Software: PyCharm


import asyncio


# 创建一个支持数据库连接的类
class AsyncContextManger:
    def __init__(self, conn=None):
        self.conn = conn

    async def get_data(self):
        return '模拟数据库增删改查...'

    async def __aenter__(self):
        # 模拟数据库连接的耗时操作 连接操作是属于网络IO
        self.conn = await asyncio.sleep(1, result='连接成功...')
        print(self.conn)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await asyncio.sleep(2)
        print('关闭数据库连接成功...')


async def main():
    async with AsyncContextManger() as fp:
        result = await fp.get_data()
        print(result)


asyncio.run(main())
