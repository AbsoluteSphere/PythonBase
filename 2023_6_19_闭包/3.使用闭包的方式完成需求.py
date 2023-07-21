def person(name):
    def say(message):
        print(f'{name}: {message}')
    print(say)
    return say  # 外层函数返回的是内部函数的引用


p1 = person('安娜')
p2 = person('双双')

p1('一起去吃饭...')
p2('好呀好呀...')

# person('夏洛')('aaa')


