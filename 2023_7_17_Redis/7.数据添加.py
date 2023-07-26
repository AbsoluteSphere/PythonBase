from redis import Redis


redis_client = Redis()
res = redis_client.set('name', '安娜')
print(res)


