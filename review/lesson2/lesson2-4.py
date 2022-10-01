# 集合
# 集合は「重複した値を持たない」、「インデックスを持たない」などの特徴がある
a = {'a', 'b', 'a', 'c', 'b'}
print(a)

a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a)
print(type(a))

b = {2, 3, 3, 6, 7}
print(b)
# a から b にあるデータを取り除いた結果
print(a-b)
# a と b に共通するデータ
print(a & b)
# + を使うとエラーになる
# print(a + b)
# a または b にあるもの
print(a | b)
# a または b にあるが、重複していないもの
print(a ^ b)

# 集合のメソッド
# addメソッドは集合にデータを追加することができる
s = {1, 2, 3, 4, 5}
s.add(6)
print(s)
# 重複した値は変化しない
s.add(4)
print(s)
# removeメソッドは集合から削除できる
s.remove(6)
print(s)
# clearメソッドで集合の中身をリセットできる
s.clear()
print(s)

# 共通の値を探すのに便利！
my_friend = {'A', 'C', 'D'}
A_friend = {'B', 'D', 'E', 'F'}
print(my_friend & A_friend)

# 重複した値を削除するために集合にすることもできる
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)