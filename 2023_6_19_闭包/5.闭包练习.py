def make_printer(message):
    def printer():
        print(message)

    return printer


# func_obj = make_printer('今天天气不错....')
# res = func_obj()
# print(res)


def print_number(num_1):
    def print_in(num_2):
        print(f'内部函数的参数为: {num_2}')
        print(f'print_in函数内存地址: {id(print_in)}')
        return f'内部函数参数与外部函数参数相加: {num_1 + num_2}'
    return print_in


func_obj = print_number(1)
res = func_obj(2)
print(f'func_obj函数内存地址: {id(func_obj)}')
print(res)
