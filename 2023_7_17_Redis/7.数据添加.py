from redis import Redis
redis_client = Redis()
# 1.添加
redis_client.hset('student', 'name', '张三')
redis_client.hset('student', 'age', '22')
redis_client.hset('student', 'address', '武汉')
redis_client.hset('student', 'habit', '看小说')
# 2.修改
redis_client.hset('student', 'habit', '看动漫')
# 3.删除
redis_client.hdel('student', 'age')
# 4.查询
data = redis_client.hgetall('student')
print(data.decode('utf-8'))
