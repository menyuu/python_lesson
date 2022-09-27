s = 'aaaaaaaaaaa'\
    + 'bbbbbbbbbbbbb'
print(s)

x = (1 + 1 + 1 + 1 + 1 + 1 + 1
    + 1 + 1 + 1 + 1 + 1 + 1 + 1)
print(x)

"""
Pythonでは80文字以上入力すると次の行にいくようにする
\でも()でも同じ挙動
"""

x = 10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('10000000000000000000')
elif x == 10:
    print('10')
else:
    print('positive')

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

a = 1
b = 1

# a が b と等しい
a == b

# a が b と異なる
a != b

# a が b よりも小さい
a < b

# a が b よりも大きい
a > b

# a が b 以下である
a <= b

# a が b 以上である
a >= b

# a も b も真であれば真
a > 0 and b > 0

# a または b が真であれば真
a > 0 or b > 0

y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

# a = 1
# b = 2
#
# if not a == b:
#     print('Not equal')
#
# if a != b:
#     print('Not equal')

is_ok = True

if not is_ok:
    print('hello')

# False, 0, 0.0, '', [](リスト), ()(タプル), {}(辞書), set()(集合) といったものに何も入っていなければFalseを返す
is_ok = []

if is_ok:
    print('OK!')
else:
    print('No!')

# None なにも値が入っていない
is_empty = None
# print(is_empty)
if is_empty is None:
    print('None!!!')

print(1 == True)
# オブジェクト同士が真であるか
# print(1 is True)
# Noneオブジェクトかどうか
print(None is None)

count = 0
while count < 5:
    print(count)
    count += 1

count = 0
while True:
    if count >= 5:
        break

    if count == 2:
        count += 1
        continue

    print(count)
    count += 1

count = 0

# この時の else は breakで抜けなければ出力される
while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print('done')

# while True:
#     word = input('Enter:')
#     num = int(word)
#     # if word == 'ok':
#     if num == 100:
#         break
#     print('next')

some_list = [1, 2, 3, 4, 5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

# for i in some_list:
#     print(i)

for s in 'abcde':
    print(s)

for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        break
    print(word)

for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate all!')

# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for i in num_list:
#     print(i)

# for i in range(2, 10, 3):
#     print(i)

for i in range(10):
    print(i, 'hello')

for _ in range(10):
    print('hello')

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks =['coffee', ' tea', 'beer']

# for i in range(len(days)):
#     print(days[i], fruites[i], drinks[i])

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

d = {'x': 100, 'y': 200}
# タプルの形で入っている
print(d.items())

for k, v in d.items():
    print(k, ':', v)

def say_something():
     # print('hi')
    s = 'hi'
    return s

# say_something()
# print(type(say_something))
# functionの型で入っているので変数に代入できる
# f = say_something
# print(f())
result = say_something()
print(result)

# 何度も呼び出すものは関数定義しておく
def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green papper'
    else:
        return "I don't know"

result = what_is_this('red')
print(result)

# 位置引数とキーワド引数を混ぜるときは順番に注意
def menu(entree='beef', drink='wine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu()
menu('chicken', drink='beer')

# Pythonでは空のリストなどの参照渡しをするようなものをデフォルト引数で渡すことを推奨しない
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(r)

y = [1, 2, 3]
r = test_func(200, y)
print(r)

r = test_func(100)
print(r)

r = test_func(100)
print(r)

def say_something(word, *args):
    print(args)
    print('word = ', word)
    for arg in args:
        print(arg)

say_something('Hi!', 'Mike', 'Nance')
# 上と同じようにできる
# t = ('Mike', 'Nancy')
# say_something('Hi!', *t)

def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

menu(entree='beef', drink='coffe')

d = {
    'entree': 'beef',
    'drink': 'ice cofee',
    'dessert': 'ice'
}
menu(**d)

# * のより後に ** をしないとエラーになる
def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu('banana', 'apple', 'orange', entree='beef', drink='coffee')

def example_func(param1, param2):
    """ファンクションの内容
        Example function with types documented in the docstring.

    どういった引数か
    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    どういった戻り値か
    Returns:
         bool: The return value.True for success, False otherwise.

    """
    print(param1)
    print(param2)
    return True

print(example_func.__doc__)

# 関数内関数
def outer(a, b):
    def plus(c, d):
        return c + d
    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)

outer(1,2)

# クロージャー
def outer(a, b):
    def inner():
        return a + b

    return inner

f = outer(1, 2)
r = f()
print(r)

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.1415192)

print(ca1(10))
print(ca2(10))

#     デコレーター
#     関数に対して前後処理ができる
#     デコレーターを使って包み込むイメージ
#     デコレーターの順番も大事
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('relust:', result)
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

@print_info
def sub_num(a, b):
    return a - b

# print('start')
# r = add_num(10, 20)
# print('end')

# f = print_info(add_num)
# r = f(10, 20)
# print(r)

r = add_num(10, 20)
print(r)

r = sub_num(100, 50)
print(r)

# ラムダ
# 簡単な関数は1行で記述できる
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     return word.capitalize()

# 上と同様の処理
# word が引数として渡される
sample_func = lambda word: word.capitalize()
change_words(l, sample_func)
print('#####################')
change_words(l, lambda word: word.capitalize())

# ジェネレーター
# ジェネレーターには return がなく yield の記述をみるとジェネレーターとして処理する
l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print('######################')

def greeting():
    yield 'Good morning'
    for i in range(20):
        print(i)
    yield 'Good afternoon'
    yield 'Good night'

def counter(num=10):
    for _ in range(num):
        yield 'run'

# for g in greeting():
#     print(g)
# 繰り返し処理のようにひとつひとつ取り出せるが間に別の処理もできる
g = greeting()
c = counter()
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
# print("あいうえお")
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
# print("かきくけこ")
print(next(g))

# リスト内包表記
# 可読性を考えて使用しないとかえって読みにくいコードになるので注意
t = (1, 2, 3, 4, 5)
t2 = (5, 6 , 7, 8, 9, 10)

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)

print(r)

# 短い forループはリスト内包表記をすると速度などのメリットがある
r = [i for i in t]
print(r)

r = [i for i in t if i % 2 == 0]
print(r)

r = []
for i in t:
    for j in t2:
        r.append(i * j)
print(r)

r = [i * j for i in t for j in t2]
print(r)

# 辞書内包表記
w = ['mon', ' tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}

for x, y in zip(w, f):
    d[x] = y

print(d)

d = {x: y for x, y in zip(w, f)}
print(d)

# 集合内包表記
s = set()
for i in range(10):
    if i % 2 == 0:
        s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)

# ジェネレーター内包表記
def g():
    for i in range(10):
        yield i

g = g()
print(type(g))
print(next(g))
print(next(g))

g = (i for i in range(10))
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# タプルの内包表記は tuple を宣言する
g = tuple(i for i in range(10))
print(type(g))
print(g)

g = (i for i in range(10) if i % 2 == 0)

for x in g:
    print(x)

# 名前空間とスコープ
animal = 'cat'

def f():
    """Test func doc"""
    # 変数を関数内で書き換えたいときは global をつける
    # global animal
    animal = 'dog'
    print('local:', locals())
    # print(f.__name__)
    # print(f.__doc__)

f()
print('global:', globals())
# print('global:', __name__)

print("##########################")
# 例外処理
l = [1, 2, 3]
i = 5
# del l

try:
    () + l
# 例外の種類
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
# Exception で受け取るのは好ましくない？
except Exception as ex:
    print('other: {}'.format(ex))
else:
    print('done')
# 必ず実行される
finally:
    print('clean up')

# 独自例外の作成
# 開発中にあえてエラーを発生させることで間違えても気づける
# raise IndexError('test error')
class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')