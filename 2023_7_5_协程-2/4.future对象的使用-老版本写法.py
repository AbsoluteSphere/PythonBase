# -*- coding: utf-8 -*-
# @Time    : 2023/7/5 9:01 下午
# @Author  : 顾安
# @File    : 4.future对象的使用-老版本写法.py
# @Software: PyCharm


import asyncio


async def work():
    print('协程启动...')
    await asyncio.sleep(1)
    return '返回值...'


async def main():
    # 在主函数中创建future对象
    future_list = [asyncio.ensure_future(work()) for _ in range(2)]
    result_list = await asyncio.gather(*future_list)
    print(result_list)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
