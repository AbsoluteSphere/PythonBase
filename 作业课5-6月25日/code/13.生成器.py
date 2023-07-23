# # 第一题 以下代码的打印结果
# def func(a):
#
#     a = a + 4
#
#     yield a
#
#     a = a - 8
#
#     yield a
#
# g=func(26)
#
# res1=next(g)
#
# print(res1)
#
# res2=next(g)
#
# print(res2)
# # 答案
# 30
# 22

# 第二题
#
# 定义一个生成器，这个生成器可以生成 1到10的奇数
# def run():
#     for i in range(1,11):
#         # print(i)
#         if i % 2 == 1:
#             # print(i)
#             yield i
# res=run()
# # print(res)
# for i in res:
#     print(i)

# 第三题
#
# 定义一个生成器，这个生成器可以生成 1 2  4 5 6  9 10
# def run():
#     start = 0
#     while start < 10:
#         start += 1
#         # print(start)
#         if start in [3,7,8]:
#             continue
#         # print(start)
#         yield start
# res=run()
# for i in res:
#     print(i)