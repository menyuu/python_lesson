# contextlib
# デコレーターに関するライブラリ

import contextlib

# def tag(name):
#     def _tag(f):
#         def _wrapper(content):
#             print('<{}>'.format(name))
#             r = f(content)
#             print('</{}>'.format(name))
#             return r
#         return _wrapper
#     return _tag

# デコレーターに引数を渡す
# @tag('h2')
# def f(content):
#     print(content)

# 2つの引数を渡す
# f = tag('h2')(f)

# f('test')


# 上記の処理が contextlib を使うことによって簡単に実装できる
@contextlib.contextmanager
def tag(name):
    print('<{}>'.format(name))
    # 関数が yield の部分で処理される
    yield
    print('</{}>'.format(name))

# 関数にデコレーターとして渡すことができる
# @tag('h2')
# def f(content):
#     print(content)
#
# f('test')

# with で渡すこともできる
# with tag('h2'):
#     print('test')

def f():
    print('test0')
    with tag('h2'):
        print('test')
        # ネストすることもできる
        with tag('h5'):
            print('test2')
    with tag('h3'):
        print('test3')

f()