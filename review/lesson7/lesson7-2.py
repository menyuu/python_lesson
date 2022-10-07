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

# Tmplate関数を利用することで元の文字列を変更してしまう可能性をなくす
# 他のチームなどが作成した文章を扱うのに有効
# openで開く
# import string

# テンプレートとなる文章を読み込み専用として扱うことによって文章の書き換えをできなくする
with open('design/email_template.txt') as f:
    # 読み込んだファイルを t に格納する
    t = string.Template(f.read())
# with文で宣言された変数(今回は "t")は、インデントの外でも使用できる
contents = t.substitute(name='Mike', contents='How are you?')
print(contents)