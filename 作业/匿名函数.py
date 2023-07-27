dic = {'k1': 10, 'k2': 200, 'k3': 20}

ret1 = max(dic, key=lambda x: dic[x])
print(ret1)  # lambda x: x 则 k3

lst = [
    {'name': 'egon', 'price': 100},
    {'name': 'rdw', 'price': 666},
    {'name': 'zat', 'price': 1}
]
ret = max(lst, key=lambda dic: dic['price'])  # 指定比较内容
print(ret)  # {'price': 666, 'name': 'rdw'}