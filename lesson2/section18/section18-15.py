# 正規表現
import re

# 文字列の分割
# # 下記の変数s のような文字列の中に英数字以外の文字が入力されていた場合は通常それも含まれる
# s = 'My name is ... Mike'
# print(s.split())
#
# # # re を使うことで英数字のみの文字列(\W で英数字以外を指定)で返す
# p = re.compile(r'\W+')
# print(p.split(s))

# 文字列の置換
p = re.compile('(blue|white|red)')
# blue や red を colour に置き換える
print(p.sub('colour', 'blue socks and red shoes'))
# 何個置き換えるかを指定できる
print(p.sub('colour', 'blue socks and red shoes', count=1))
# 何個置き換えたか調べたい場合
print(p.subn('colour', 'blue socks and red shoes'))

def hexrepl(match):
    value = int(match.group())
    # 16新数にする
    return hex(value)

p = re.compile(r'\d')
print(p.sub(hexrepl,'12345 11 22 99990000 test test2'))

