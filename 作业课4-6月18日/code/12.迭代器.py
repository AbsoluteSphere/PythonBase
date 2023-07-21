# 第一题（单选题）
#
# 下列哪一种是不可迭代的
#
#     A.int
#
#     B.str
#
#     C.list
#
#     D.set

# 答案
#
# A

# 第三题（单选题）
#
# 以下哪个异常用于标识迭代的完成
#
#     A.StopIteration
#
#     B.NameError
#
#     C.KeyError
#
#     D.IndexError
#
# 答案
#
# A
# iter_1=[1,2,3].__iter__()
# print(iter_1.__next__())
# print(iter_1.__next__())
# print(iter_1.__next__())
# print(iter_1.__next__())

#
# 选做题
#
# 第五题
#
# 以下代码的打印结果是

obj_iter = [1,2,3,4,5,6,7,8,9]
# obj_iter可迭代对象编程obj_next迭代器
obj_next=obj_iter.__iter__() # obj_iter毛坯房 变成了一手新房
print(obj_next)
print(obj_next.__next__())# 迭代器obj_next被取走了一个1 # 变成了二手新房
print(obj_next.__next__())# 迭代器obj_next被取走了一个2 # 变成了三手新房
for i in obj_iter:# 是一个全新的迭代器  obj_iter它是一个毛坯房   新房：迭代器
    print(i)
# 之前被取掉了 1 ，2 这2个数据  obj_next剩下3,4,5,6,7,8,9 # 变成了四手新房
for i in obj_next:
    print(i)

