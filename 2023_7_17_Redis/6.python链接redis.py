# 导包
from redis import Redis

# 1. 创建链接
db = Redis()

# 2. 打印链接对象 在链接的过程中建议使用异常捕获
print(db)

