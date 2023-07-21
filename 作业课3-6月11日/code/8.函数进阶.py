# 第二题
#
# 关于函数的参数使用限制，以下选项中描述错误的是（ ）
#
#     A.关键字参数必须位于位置参数之前
#     B.关键字参数必须位于位置参数之后
#     C.关键字参数顺序无限制
#     D.位置形参限制了实参的传参个数
#
# def run(a,b):
#     print(a,b)
#
# run(1,2)
# run(1,b=2)
# 错误演示
# run(a=1,2)
# 答案
#
# A

'''
第三题

定义一个函数，可以完成以下国家汇率的计算，要求输入是各国的金额，输出的是中国人民币的金额

各国汇率如下：美元6.84，欧元8.12，日元0.06，港元0.88，澳元4.98

例如输入美元，金额100，兑换成人民币是100*6.84=684元

答案


'''
def run(str1,money):
    # print(str1,money)
    # pass
    #  如果找到了就返回索引，索引它一定不等于-1
    if str1.find('美')!=-1:
        money = money * 6.84
    elif str1.find('欧')!=-1:
        money = money * 8.12
    elif str1.find('日')!=-1:
        money = money * 0.06
    elif str1.find('港')!=-1:
        money = money * 0.88
    elif str1.find('澳')!=-1:
        money = money * 4.98
    else:
        print('抱歉不支持转换')
    print('%.2f'%money)
str1 = input('输入你想转换的国家')
money = float(input('输入你想换算的金额'))
run(str1,money)







