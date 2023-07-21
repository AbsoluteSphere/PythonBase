def my_range(num):
    i = 0
    while i < num:
        # 如果一个函数中出现了yield关键字 则这个函数是一个生成器函数
        yield i
        i += 1


obj = my_range(5)
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
for i in obj:
    print(i)


# 如何判断指定的方式在指定的类中是否实现
print(hasattr(obj, '__iter__'))
print(hasattr(obj, '__next__'))
