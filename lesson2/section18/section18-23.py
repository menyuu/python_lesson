import functools

# def f(x, y):
#     return x + y

# def task(f):
#     print('start')
#     # print(f(10, 20))
#     print(f())
#
# def outer(x, y):
#     def inner():
#         return x + y
#     return inner


# task(f)
# task(lambda x, y: x + y)
# f = outer(10, 20)
# print(outer(10, 20))
# task(f)

# 上記の処理を簡単に書く
def f(x, y):
    return x + y

def task(f):
    print('start')
    print(f())

p = functools.partial(f, 10, 20)
task(p)