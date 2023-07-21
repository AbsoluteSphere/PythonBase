
def my_wrapper(func_obj):
    def wrapper(name):
        print('装饰器已经启动...')
        func_obj(name)

    return wrapper


# @my_wrapper
def my_func_print(name):
    print(f'{name}')


func_obj = my_wrapper(my_func_print)
func_obj('安娜')
