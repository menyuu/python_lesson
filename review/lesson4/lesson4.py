# 関数
# 関数は呼び出しより先に定義しておかないとエラーが返る
# 関数の定義
def say_something():
    print('hi')

# 関数の呼び出し
say_something()
# 型の確認
print(type(say_something))
# 関数にもオブジェクトなので変数に入れることができる
f = say_something
f()

# 返り値(戻り値)
# 関数で何か値を呼び出し元に返したい場合は return を使う
def say_something():
    s = 'hi'
    # 変数 s を呼び出し元に返す
    return s

result = say_something()
print(result)

# 引数
# 関数の処理に必要なデータ
def what_is_this(color):
    print(color)

what_is_this('red')

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return  'green pepper'
    else:
        return  "I don't know"

result = what_is_this('red')
print(result)

# 位置引数
# 引数と仮引数で渡したいデータの記述する位置を同じにしていないと予期せぬデータが返ってくるので注意が必要
def menu(entree, drink, dessert):
    print('entree =',entree)
    print('drink =', drink)
    print('dessert =', dessert)

menu('beef', 'beer', 'ice')

# キーワード引数
# 引数で引数名と値を指定する
# 引数と仮引数の位置が違っていても対応できる
def menu(entree, drink, dessert):
    print('entree =', entree)
    print('drink =', drink)
    print('dessert =', dessert)

menu(dessert='ice', drink='beer', entree='beef')
# 位置引数とキーワード引数と混ぜて使うと位置引数が正しい位置にない場合エラーが返る
# menu(dessert='ice', beef, drink='beer')

# デフォルト引数
# 引数で値の指定がない場合、仮引数で先に決めておいた値を代入してデータを渡す
def menu(entree='beef', drink='beer', dessert='ice'):
    print('entree =', entree)
    print('drink =', drink)
    print('dessert =', dessert)

menu()

# リストや辞書などの参照渡しするものをデフォルト引数にする場合、2度目以降に呼び出したら同じアドレスから参照してしまうので注意
def sample_func(x, l=[]):
    l.append(x)
    return l

r = sample_func(100)
print(r)
r = sample_func(100)
print(r)

# 解決するには？
# デフォルト引数にNoneを指定して、リストがNoneであれば初期化する処理するコードを書く
def sample_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = sample_func(100)
print(r)
r = sample_func(100)
print(r)

# 引数の数が多くなったりわからない場合は？
# * を付けた引数にすると複数の引数をタプルでまとめてくれる
def say_something(*args):
    print(args)

say_something('Hi!', 'Mike', 'Nancy')

def say_something(*args):
    for arg in args:
        print(arg)

say_something('Hi!', 'Mike', 'Nancy')

def say_something(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)

say_something('Hi!', 'Mike', 'Nancy')

# 引数を渡すときにアンパッキングする
# アンパッキング・・・リストやタプルなどを複数の値として展開する
# list = [1, 2, 3]
# print(*list)
def say_something(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)

# 呼び出しの時にアンパッキングできる
t = ('Mike', 'Nancy')
say_something('Hi!', *t)

# キーワード引数の辞書化
# ** のように引数の前に * を２つ付けることによってキーワド引数を辞書型で受け取れる
def menu(**kwargs):
    print(kwargs)

menu(entree='beef', drink='coffee')

def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

menu(entree='beef', drink='coffee')

# キーワード引数を辞書型にして渡す場合
def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}
# アスタリスク2つを付けて辞書型として渡すことができる
menu(**d)

# 位置引数, タプル化, 辞書化を組み合わせて使うこともできる
# * は ** よりも前に書かないとエラーになるので注意
def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu('banana', 'apple', 'orange', entree='beef', drink='coffee')

# docstring とは？
# 関数の説明文
def example_func(param1, param2):
    """
    関数の説明
    Docstring example for describing overall explanation of function.

    引数の説明
    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    返り値の説明
    Returns:
         bool: The return value. Trhe for success, False otherwise.
    """
    print(param1)
    print(param2)
    return True

# .__doc__ や help で確認することができる
print(example_func.__doc__)
help(example_func)