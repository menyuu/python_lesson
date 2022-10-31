# 正規表現
# ドキュメントと照らし合わせながら使うことが多い
import re


# a と c の間にあるドット(.)は任意の１文字
# a と c が含まれている間が任意の１文字でなければ None を返す
m = re.match('a.c', 'abc')
# m = re.match('a.c, 'a') == None
# m = re.match('a.c, 'bbc') == None
# m = re.match('a.c, 'abdbdbdbdbdbdc') == None
print(m)
# m.group() で中身を確認できる
print(m.group())

# 文中に含まれているかどうかを探して返す
# m = re.search('a.c', 'test abc test')
m = re.search('a.c', 'fklwsjhfgojwaergfjabcgiokwjgoiawjg')
print(m)
print(m.group())
# m.span() で探した文字列のインデックスを返してくれる
print(m.span())
m = re.search('a.c', 'test abc abc test')
# 同じ文字列か含まれていても一番最初の文字列を探して返す
print(m)

# マッチする部分をすべて探す場合には findall を使う
m = re.findall('a.c', 'test abc abc test')
print(m)

# イテレーターにして返す
m = re.finditer('a.c', 'test abc abc test')
print(m)
# イテレーターで返ってきているので for文でループを回せる
# print([w.span() for w in m])
print([w.group() for w in m])

# ? は b が 0回か1回マッチするかどうかを判定
# m = re.match('ab?', 'a')
# m = re.match('ab?', 'ab')
# 2回目の b は判定されない
m = re.match('ab?', 'abb')
print(m)

# アスタリスク(*)は0回以上の繰り返しを判定
# m = re.match('ab*', 'a')
# m = re.match('ab*', 'ab')
m = re.match('ab*', 'abbbb')
print(m)

# プラス(+)は1回以上の繰り返し
# m = re.match('ab+', 'a') == None
# m = re.match('a+b+', 'aaabb')
m = re.match('ab+', 'abbbbb')
print(m)

# マッチする回数を指定できる
# m = re.match('a{3}', 'a')　== None
m = re.match('a{3}', 'aaa')
print(m)
# マッチする範囲を指定できる
m = re.match('a{2,4}', 'aaa')
print(m)
# 先頭からの範囲になる
m = re.match('a{2,4}', 'aaaaa')
print(m)

# 集合(今回は a~c の範囲を指定している)
# a~c の1文字
# m = re.match('[a-c]', 'a')
m = re.match('[a-c]', 'cafe')
print(m)
# アルファベット全体から探したい場合
m = re.match('[a-zA-z]', 'x')
print(m)
# 数字を探したい場合
m = re.match('[a-zA-z0-9]', '5')
print(m)
# アンダースコア(_)を探したい場合
m = re.match('[a-zA-z0-9_]', '_')
print(m)
# 任意の英数もしくはアンダースコア(_)文字を探したい場合はバックスラッシュ(\)と小文字の w
# 上記と同じ処理
m = re.match('\w', '_')
# m = re.match('\w', '@') == None
print(m)
# 英数文字以外から探したい場合はバックスラッシュ(\)と大文字の w
# m = re.match('\W', '@')
m = re.match('\W', '-')
print(m)
# 上記と同じ処理
m = re.match('[^a-zA-z0-9_]', '@')
print(m)
# 数字のみを探したい場合
m = re.match('\d', '2')
print(m)
# 数字以外を探したい場合
m = re.match('\D', 'a')
print(m)
# a または b などを探したい場合
m = re.match('a|b', 'a')
print(m)
# abc などのかたまりを探したい場合
# プラスがあるので1回以上
m = re.match('(abc)+', 'abcabcabc')
# m = re.match('(abc)+', 'aaaabccccc') == None
print(m)
# スペースを探したい場合
m = re.match('\s', ' ')
print(m)
# スペース以外を探したい場合
m = re.match('\S', 'a')
print(m)
# * や + といった正規表現で使うものを探したい場合は \ を入れる
m = re.match('\*', '*')
print(m)
m = re.match('\?', '?')
print(m)

# ^ をつけることによって先頭が指定した文字から始まる文字列を探す
# m = re.search('^abc', 'test abc') == None
m = re.search('^abc', 'abc test abc')
print(m)
# $ をつけることによって最後が指定した文字で終わる文字列を探す
m = re.search('abc$', 'test abc')
# m = re.search('abc$', 'test abc test') == None
print(m)