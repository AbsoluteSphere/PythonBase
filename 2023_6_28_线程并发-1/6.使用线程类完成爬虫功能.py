# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 9:31 PM
# @Author  : 顾安
# @File    : 6.使用线程类完成爬虫功能.py
# @Software: PyCharm


import requests
import threading


class ThreadSpider(threading.Thread):
    def __init__(self, image_url):
        super().__init__()
        self.image_url = image_url

    # 启动线程时start方法会自动调用run方法
    def run(self):
        response = requests.get(self.image_url).content
        file_name = self.image_url.rsplit('/')[-1]
        with open(file_name, 'wb') as file:
            file.write(response)
            print('下载完成...')


url_list = [
    'http://pic.bizhi360.com/bbpic/98/10798.jpg',
    'http://pic.bizhi360.com/bbpic/92/10792.jpg',
    'http://pic.bizhi360.com/bbpic/86/10386.jpg'
]


for url in url_list:
    t = ThreadSpider(url)
    t.start()

