def logging(level):
    def wrapper(func):# 第二内层的函数
        def inner_wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper# 获得了最内层的函数地址
    return wrapper


# @logging(level='INFO')
def say(something):
    print("say {}!".format(something))


# 如果没有使用@语法，等同于
wrapper = logging(level='INFO')
print(wrapper)
say = wrapper(say)
# say = logging(level='INFO')(say)


say('hello')
