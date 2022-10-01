# 変数
num = 1
print(num, type(num))
name = 'Mike'
print(name, type(name))
is_ok = True
print(is_ok, type(is_ok))
# 変数に違う型の変数を代入すると型が変わる
num = name
print(num, type(num))

# 文字列を数値に型変換
name = '1'
new_name = int(name)
print(new_name, type(new_name))

# 型の宣言をしても代入などによって型が変更されてしまう
num: int = 1
name: str = '1'

num = name

print(num, type(num))

# 数字や予約語のようなものは変数として扱えない

# print関数
# sepによってカンマ区切りにする場合は sep=',' のようにする
print('Hi', 'Mike', sep=',')
# 終わりの文字は'\n'(改行)になっているので改行なしに指定することも可能
print('Hi', 'Mike', sep=',', end='')
print('Hi', 'Mike', sep=',', end='\n')

# math関数
import math
# 平方根の計算
result = math.sqrt(25)
print(result)
# 対数の計算
result = math.log2(10)
print(result)
# help関数を使うことによってドキュメントを確認することができる
# print(help(math))

# シングルクォート(ダブルクォート)の中にシングルクォート(ダブルクォート)入れる場合はバックスラッシュを入れる
print('I don\'t know')
print("say \"I don't know\"")
# 文の途中で改行を入れる場合は正規表現(\n)で改行する
print('hello. \nHow are you?')
# pathなどで改行が起こる場合はrawデータとして記述する
print(r'C:\name\name')
# 複数行改行する場合はダブルクォート3つずつで囲む
print("##########")
print("""
line1
line2
line3
""")
print("##########")
# そのままだと改行が入ってしまうのでダブルクォートの続きから記述するかバックスラッシュを入れる
print("##########")
print("""\
line1
line2
line3\
""")
print("##########")

# 文字列の連結
# 同じ文字列を繰り返す
print('Hi.' * 3)
print('Hi.' * 3 + 'Mike')
# 文字列の連結
print('Py' + 'thon')
print('Py''thon')
# 変数と文字列を連結する場合は(+)が必要
prefix = 'Py'
# print(prefix'thon') このようにはできない
print(prefix + 'thon')
# 複数行の文字列の連結
# 連結したい文字列を()で囲むかバックスラッシュで区切る
s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)
s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'\
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
print(s)

# インデックスとスライス
# 文字列は頭から順番に0～インデックスが振り分けられている
word = 'python'
print(word[0])
print(word[1])
# 後ろからの場合は[-1]から指定できる
print(word[-1])
# スライスは〇番目から〇番目というような指定ができる
print(word[0:2])
print(word[2:5])
# 最初や最後のインデックスは省略できる
print(word[:2])
print(word[2:])
# インデックスが存在しない場合は指定できないので注意
# print(word[100])
# 文字列の一部を書き換えられない
# word[0] = j
# 変更する場合は他の指定も必要
change_word = 'j' + word[1:]
print(change_word)
# len関数用いると長さを取得できる
n = len(word)
print(n)
print(len('python'))

# メソッド
# 文字列の後にドット(.)をつけて実行する
# 使えるメソッドは変数の型によって違う
# startswithメソッドは引数で渡した文字列で始まっているかどうかを調べられる
s = 'My name is Mike. Hi Mike'
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print((is_start))
# findメソッドは引数で渡した文字列が何番目から始まるかを調べられる
print(s.find('Mike'))
# rfindメソッドはfindメソッドの逆で後ろから何番目から始まるかを調べられる
print(s.rfind('Mike'))
# countメソッドは引数で渡した文字列が何個存在するかを調べられる
print(s.count('Mike'))
# capitalizeメソッドは文字列の最初を大文字、それ以外を小文字に変換してくれる
print(s.capitalize())
# titleメソッドは単語の最初の文字を大文字、それ以外を小文字に変換してくれる
print(s.title())
# upperメソッドは全てを大文字に変換してくれる
print(s.upper())
# lowerメソッドは全てを小文字に変換してくれる
print(s.lower())
# replaceメソッドは第一引数に渡した文字列と第二引数に渡した文字列を置換してくれる
print(s.replace('Mike', 'Nancy'))

# format
# f-strings
a = 'a'
print(f'a is {a}')
x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')
name = 'Taro'
family = 'Tanaka'
print(f'My name is {name} {family}. Watashi wa {family} {name}.')

