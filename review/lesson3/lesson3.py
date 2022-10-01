# 条件分岐
x = -10
if x < 10:
    print('negative')

x = 10
if x < 0:
    print('negative')
else:
    print('positive')

x = 0
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

x = 10
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x ==10:
    print(10)
else:
    print('positive')

# if文は上から読み込まれるので最初に当てはまったものから実行されるため注意がいる
x = 10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('100000000')
elif x == 10:
    print('10')
else:
    print('negative')

# 比較演算子
a = 1
b = 1

print(a == b)
print(a != b)
print(a < b)
print(a <= b)
if a > 0 and b > 0:
    print('a and b are positive')
if a > 0 or b > 0:
    print('a or b are positive')

y = [1, 2, 3]
x = 1

# in と not の使い方
if x in y:
    print('in')

if not 100 in y:
    print('not in')

a = 1
b = 10

if not a == b:
    print('Not equal')
# 上記と全く同じ処理になるため、ワンクッションある上記の処理は推奨されていない
if a != b:
    print('Not equal')

# Boolean型などでは not を用いられることが多い
is_ok = True
if is_ok:
    print('hello')
if not is_ok:
    print('hello')
else:
    print('not ok')

# 値が入ってないことを確認する方法
is_ok = True

if is_ok:
    print('OK!')
else:
    print('No!')

# 0以外の数値を代入している場合
is_ok = 1

if is_ok:
    print('OK!')
else:
    print('No!')

# 0を代入している場合
is_ok = 0

if is_ok:
    print('OK!')
else:
    print('No!')

# 文字列が代入されている場合
is_ok = 'aiueokakikukeko'

if is_ok:
    print('OK!')
else:
    print('No!')

# 空の文字列が代入されている場合
is_ok = ''

if is_ok:
    print('OK!')
else:
    print('No!')

# リストの場合
is_ok = [1, 2, 3]

if is_ok:
    print('OK!')
else:
    print('No!')

is_ok = []

if is_ok:
    print('OK!')
else:
    print('No!')

# 何も入っていない状態を表す None について
is_empty = None
# print(help(is_empty))

if is_empty == None:
    print('None!!!')

# 上記の書き方は推奨されていなく None であることの判定をするには is を使用する
if is_empty is None:
    print('None!!!')

if is_empty is not None:
    print('None!!!')

# オブジェクト同士の判断
print(1 == True)
# 1 is True では False を返す
print(1 is True)
print(True is True)

print(None is None)
