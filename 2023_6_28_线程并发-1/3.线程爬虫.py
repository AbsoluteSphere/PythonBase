# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 8:18 PM
# @Author  : 顾安
# @File    : 3.线程爬虫.py
# @Software: PyCharm


"""
通过线程的方式在网络中抓取一些图片
"""

import requests
import threading


# 爬虫函数
def get_image(url):
    response = requests.get(url).content

    file_name = url.rsplit('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response)
        print('下载完成...')


url_list = [
    'http://pic.bizhi360.com/bbpic/98/10798.jpg',
    'http://pic.bizhi360.com/bbpic/92/10792.jpg',
    'http://pic.bizhi360.com/bbpic/86/10386.jpg'
]

# for url in url_list:
#     get_image(url)

"""
目前的爬虫执行过程是:
    先去下载第一个图片并写入完成后才能下载第二张图片
"""

"""
使用线程的方式完成图片下载
"""
for url in url_list:
    # 创建线程对象
    t = threading.Thread(target=get_image, args=(url,))
    # 启动线程
    t.start()

