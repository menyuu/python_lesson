# ファイルの便利な活用方法
# $マークへの代入
# Template関数(標準ライブラリの string をインポートすると利用可能)
import string

s = """\
Hi $name.
$contents
Have a good day
"""

t = string.Template(s)
# substituteメソッドの引数に $ で始まる部分に代入する文字列を指定
contents = t.substitute(name='Mike', contents='How are you?')
print(contents)