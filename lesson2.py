r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3)) #3つ目のインデックスから後にある3を探す

print(r.count(3)) #3の個数

if 5 in r:
    print('exist')

if 100 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)
# to_split = s.split('!!!')
# print(to_split) #splitメソッドの引数に存在しない値を渡せば、そのままリストに代入される

x = ' '.join(to_split)
print(x)

print(help(list))

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j =', j)
print('i =', i)

x = [1, 2, 3, 4, 5]
y = x.copy()
# y = x[:] 上と同様の処理
y[0] = 100
print('y = ', y)
print('x =', x)

print('###########')

x = 20
y = x
y = 5
print(id(x))
print(id(y))
print(y)
print(x)

x = ['a', 'b']
y = x
y[0] = 'p'
print(id(x))
print(id(y))
print(y)
print(x)

# tupleは読込専用

num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = 10, 20
print(x, y)

min, max = 0, 100
print(min, max)

#長くなりすぎることのないように注意
# a, b, c, d, e, f, g = 'aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg'
# print(a, b, c, d, e, f, g)

i = 10
j = 20
tmp = i
i = j
j = tmp

print(i,j)

a = 100
b = 200

a, b = b, a
print(a, b)

chose_from_two = ('A', 'B','C')

answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)
# タプルにすることで間違えて変数に入れてしまうことを防ぐ
# タプルにappendできないのでエラーが出るのでバグを防ぐ

x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

l = [
    ['apple', 100],
    ['banana', 200],
    ['orange', 300],
]
# すぐに探せない

fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}
# 本の目次のイメージ
print(fruits['apple'])

my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)
# リストからセットに型変換が可能
# 重複するデータを省くことができる