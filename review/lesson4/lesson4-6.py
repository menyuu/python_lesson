# 内包表記
# 内包表記にすることで処理を簡単にできるが読みにくくなる場合があるので注意
# リスト内包表記
# タプルからリストを作る
t = (1, 2, 3, 4, 5)

r = []
for i in t:
    r.append(i)

print(r)

# 内包表記でリストを作る
t = (1, 2, 3, 4, 5)
r = [i for i in t]
print(r)

# 内包表記の比較
# 偶数をリストに代入
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
r = []
for i in t:
    if i % 2 == 0:
        r.append(i)

print(r)

# appendしていないので速度が速いメリットがあるが、複雑なループが内包表記で書くとかえって読みにくくなるので注意
# 短いループなどはリスト内包表記で書いてもよい
# 後ろに if を付けることができる
r = [i for i in t if i % 2 == 0]

print(r)

# 2つの forループのリスト内包表記
t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8 ,9, 10)

# 通常のループ
r = []
for i in t:
    for j in t2:
        r. append(i * j)

print(r)

# 内包表記
# 処理の内容を[]の中に書く
r = [i * j for i in t for j in t2]
print(r)

# 辞書内包表記
# 通常のループ
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

# 内包表記
# キーとバリューをコロン(:)でつなぐ
d = {x: y for x, y in zip(w, f)}
print(d)

# 集合内包表記
# 通常のループ
s = set()

for i in range(10):
    s.add(i)

print(s)

# 内包表記
# 集合なので{}
s = {i for i in range(10)}
print(s)

# if文を使った場合
s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)

# ジェネレーター内包表記
# 通常のループ
def g():
    for i in range(10):
        yield i
g = g()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# ジェネレーター内包表記
# ()を使う
g = (i for i in range(10))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(type(g))

# 内包表記でタプルを作る場合
# tuple を宣言する
g = tuple(i for i in range(10))
print(type(g))
print(g)

# ジェネレーター内包表記の if文
g = (i for i in range(10) if i % 2 == 0)
for x in g:
    print(x)