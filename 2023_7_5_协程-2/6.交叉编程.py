# -*- coding: utf-8 -*-
# @Time    : 2023/7/5 9:15 下午
# @Author  : 顾安
# @File    : 6.交叉编程.py
# @Software: PyCharm

import asyncio
import requests


async def get_image(image_url):
    print('开始下载: ', image_url)
    # 获取一个运行的事件循环
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, requests.get, image_url)  # 默认创建线程池执行不支持async的任务

    # run_in_executor创建的线程池所返回的对象是支持协程await的
    response = await future

    file_name = image_url.rsplit('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response.content)


image_url_list = [
    'http://pic.bizhi360.com/bbpic/98/10798.jpg',
    'http://pic.bizhi360.com/bbpic/92/10792.jpg',
    'http://pic.bizhi360.com/bbpic/86/10386.jpg'
]

# 创建事件循环
loop = asyncio.get_event_loop()
tasks = [loop.create_task(get_image(url)) for url in image_url_list]
loop.run_until_complete(asyncio.wait(tasks))

