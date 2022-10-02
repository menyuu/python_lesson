# デコレーター
# デコレーターを定義すると別の関数を作成した際にも、 @ を記述するだけで利用できる
# 実行前と実行後に処理を行う
def add_num(a, b):
    return a + b

# このような関数を実行する前後に処理を加えたいときはデコレーターを使用する
print('start')
r = add_num(10, 20)
print('end')

print(r)

# デコレーターの作成
# 引数にfunc関数を指定する
def print_info(func):
    # 関数内関数の作成
    # 引数はなんでも受け取れるようにする
    def wrapper(*args, **kwargs):
        # 処理の前後に行いたい処理を前後に書く
        print('start')
        # func関数に *args と **kwargs を渡す
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def add_num(a, b):
    return a + b

# print_info関数の引数に add_num関数を渡す
f = print_info(add_num)
# add_num関数の引数として(引数 func の引数として)関数内関数の引数に渡す引数
# 1度目の呼び出しでは wrapper関数は実行されない
r = f(10, 20)
print(r)

# 上記の処理と同様の可読性の高いデコレーターの記述
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

# 別のデコレーターを作成
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

# 複数のデコレーター
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

# 複数のデコレーターを記述する場合は先に実行したいデコレーターから順番に記述する
@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

# @print_more と @print_info を逆転させた場合、@print_more の間に @print_info が実行されている
@print_more
@print_info
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

# デコレーターを使わずに複数のデコレーターを記述する場合
def add_num(a, b):
    return a + b

f = print_info(print_more(add_num))
r = f(10, 20)
print(r)