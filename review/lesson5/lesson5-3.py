# 標準ライブラリ
# collectionsライブラリ defaultdict
s = 'gklsrjglkwrjgksrhgpwj'

# 通常のループ
d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1

print(d)

# setdefault
# キーに対応する値が入っていない場合は値を入れる
d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1

print(d)

# defaultdict
# 初期値が 0 の defaultdict型を作ってくれる

from collections import defaultdict
# int を指定して初期値を0にする
d = defaultdict(int)
for c in s:
    d[c] += 1

print(d)
print(type(d))