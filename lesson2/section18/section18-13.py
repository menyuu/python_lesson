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

