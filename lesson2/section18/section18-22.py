import functools

def d(f):
    def w():
        """ Wrapper docstring"""
        print('decorator')
        return f()
    return w

@d
def example():
    """ Example docstring"""
    print('example')

example()

# help で読み込んだ場合、example という関数は d関数に渡して処理をしているので
# w() が帰ってくるようになっている
print(example.__doc__)
help(example)

print('#######################################')

# デコレーターがついた呼び出した関数の doc などを呼び出したい場合、
# functools.wraps() を使うことで、呼び出した関数の doc などを表示できる
def d(f):
    @functools.wraps(f)
    def w():
        """ Wrapper docstring"""
        print('decorator')
        return f()
    return w

@d
def example():
    """ Example docstring"""
    print('example')

print(example.__doc__)
help(example)
