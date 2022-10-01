# タプル
# タプルは値を書き換えられない
# タプルに入っているリストの中身は変更できる
t = ([1, 2, 3], [4, 5, 6])
print(t)
t[0][0] = 100
print(t)

# タプルのアンパッキング
# 複数の変数に対しタプルの中身を展開して代入することができる(アンパッキング)
# アンパッキングする変数が多くなるとかえってわかりにくくなるので注意が必要
num_tuple = 10, 20
x, y = num_tuple
print(x, y)
# アンパッキングは変数に代入された値の入れ界に便利！
# 通常
i = 10
j = 20
tmp =i
i = j
j = i
print(i, j)
# アンパッキング
a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)

# タプルは変更できないので append などによって値を変更してしまうリスクを抑えられる
choose_from_three = ('A', 'B', 'C')

answer = []

answer.append('A')
answer.append('B')

print(choose_from_three)
print(answer)

# リストを使って間違って append してしまった場合
choose_from_three = ['A', 'B', 'C']

answer = []

choose_from_three.append('A')
choose_from_three.append('C')

print(choose_from_three)

# タプルだとエラーが返る
# choose_from_three = ('A', 'B', 'C')
#
# answer = []
#
# choose_from_three.append('A')
# choose_from_three.append('C')
