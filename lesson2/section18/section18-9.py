import collections

d = {}
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    if word not in d:
        d[word] = 0
    d[word] += 1
print(d)

# 簡単に書く場合
d = {}
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    d.setdefault(word, 0)
    d[word] += 1
print(d)

# defaultdict で int型を初期値として扱う場合
d = collections.defaultdict(int)
l = ['a', 'a', 'a', 'b', 'b', 'c']
for word in l:
    d[word] += 1
print(d)

# 集合でも defaultdict を使うことができる
d = collections.defaultdict(set)
# タプルで値を書いて集合にする
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
for k, v in s:
    # set になっているので add で入れる
    d[k].add(v)
print(d)


l = ['a', 'a', 'a', 'b', 'b', 'c']
# 要素の数をカウントしてくれるメソッド
c = collections.Counter()
for word in l:
    c[word] += 1
print(c)
# 引数に入れた数を多い数からランキングのように探す
print(c.most_common(1))
# 上から 3つ探す
print(c.most_common(3))
# 値だけ返す
print(c.values())
# 全て足すには
print(sum(c.values()))

# ファイルの中身から一番多いものを探す
import re
with open('section18-10.py', 'r') as f:
    # \w はアルファベットと数字の文字列を探す
    # + をつけることによって1文字以上
    # 文字列をリストとして代入する
    words = re.findall(r'\w+', f.read().lower())
    print(words)
    print(collections.Counter(words).most_common(20))