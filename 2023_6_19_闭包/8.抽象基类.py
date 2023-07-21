
from abc import ABC, abstractmethod


# 手写一个web框架 支持缓存
class Cache(ABC):
    # 如果想要在缓存中获取数据
    @abstractmethod
    def get_data(self):
        pass

    # 如果想要修改缓存中的数据
    @abstractmethod
    def set_data(self, value):
        pass






