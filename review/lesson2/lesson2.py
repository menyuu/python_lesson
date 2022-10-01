# リスト
r = [1, 2, 3, 4, 5, 1, 2, 3, 0]
# indexメソッドは引数で渡した値が何番目のインデックスにあるかを調べてくれる
print(r.index(3))
# 第二引数に指定したインデックスから調べる
print(r.index(2, 3))
# countメソッドは引数で指定した値が何個存在するかを調べてくれる
print(r.count(3))
# in の前に指定したものが in のあとに指定したものに含まれているかを調べる
if 5 in r:
    print('exist')
# sortメソッドは小さい順にソートする
r.sort()
print(r)
# reverse=True にする、もしくは reverseメソッドを使うことで降順になる
r.sort(reverse=True)
print(r)
r.sort()
print(r)
r.reverse()
print(r)
# splitメソッドは引数で指定した文字列で分割できる
s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)
# 指定した文字列が存在しない場合はそのまま返す
# to_split =s.split('!!!')
# print(to_split)
# joinメソッドは分割されている文字列を結合できる
x = ' '.join(to_split)
print(x)
# helpメソッド
# print(help(list))

# リストをコピーするときの注意点
# リストを格納した変数を他の変数に代入し、代入した変数から値を変更する場合は元になったリストの値も変更されてしまう
# リストは値渡しではなく、参照渡しによって値が代入するから起こる
i = [1, 2, 3, 4, 5]
j =i
j[0] = 100
print('j = ', j)
print('i = ', i)
# 値を変更する場合などにはcopyメソッドでコピーして変更する
x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('y = ', y)
print('x = ', x)
# 文字列や整数などは値渡しで、リストや辞書などは参照渡しということを理解しなければバグに繋がるので注意
# 値渡しされたものはidそのものが変更されるが参照渡しされたものは同じidで割り当てられる
# 整数の場合
x = 20
y = x
y =5
print('y = ', y)
print('x = ', x)
print('y = ', id(y))
print('x = ', id(x))
# リストの場合
x = ['a', 'b']
y = x
y[0] = 'p'
print('y = ', y)
print('x = ', x)
print('y = ', id(y))
print('x = ', id(x))
