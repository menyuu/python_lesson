# 繰り返し
# while文では1回繰り返すごとに数値を加算しないと無限ループが起こるので注意
count = 0
while count < 5:
    print(count)
    count += 1

# break文
# break することによってループを抜けることができる
count = 0
while True:
    if count >= 5:
        break
    print(count)
    count += 1

# continue文
# continue でスキップする
count = 0
while True:
    if count >= 5:
        break
    if count == 2:
        count += 1
        continue
    print(count)
    count += 1

# ループ文のあとにelseを入れることによってループ後の処理を記述することができる
# break した場合 else は処理されないので注意
# break した時に実行したくない処理がある場合は else が有効
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('Done')

# input関数
# 標準入力
# while True:
#     word = input('Enter')
#     if word == 'ok':
#         break
#     print('next')
#
# while True:
#     word = input('Enter')
#     num = int(word)
#     if num == 100:
#         break
#     print('next')

# for文
# while文との比較
some_list = [1, 2, 3, 4, 5]

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

some_list = [1, 2, 3, 4, 5]
for i in some_list:
    print(i)

# for文
for s in 'abcde':
    print(s)

for word in ['My', 'name', 'is', 'Mike']:
    print(word)

for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        break
    print(word)

for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        continue
    print(word)

for fruit in ['apple', 'banana', 'orange']:
    print(fruit)
else:
    print('I ate all.')

for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate all.')

# range関数
# 回数が決まっているループの処理に使用する関数
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in num_list:
    print(i)

# 上記と同様の処理
for i in range(10):
    print(i)

# 2から10まで
for i in range(2, 10):
    print(i)

# 2から10まで3飛ばし
for i in range(2, 10, 3):
    print(i)

# 同じ処理を繰り返したい場合
for i in range(10):
    print('hello')
# ただ繰り返したい場合は変数に i ではなくアンダースコア(_)を使用すれば明示することができる
for _ in range(10):
    print('hello')

# enumerate関数
# インデックス番号も取り出すことができる
# 通常の場合
i = 0
for fruit in ['apple', 'banana', 'orange']:
    print(i, fruit)
    i += 1
# enumerate関数を使うとカウントなどをしなくてもよい
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

# zip関数
# 複数のリストをひとまとめにして可読性を高くする
# 読みにくい
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

# 読みやすい
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

# 辞書のfor文
# キーのみ
d = {'x': 100, 'y': 200}
for v in d:
    print(v)

# itemsメソッドを使用する
d = {'x': 100, 'y': 200}

for k, v in d.items():
    print(k, ':', v)
# itemsの中身
print(d.items())