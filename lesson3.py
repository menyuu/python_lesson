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
print(1 is True)
# Noneオブジェクトかどうか
print(None is None)