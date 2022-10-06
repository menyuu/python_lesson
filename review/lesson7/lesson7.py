# ファイルの作成
# open関数にファイル名とモードを指定する
# 'w'モードは write(書き込み)モード
f = open('test.txt', 'w')
# writeメソッドで内容の書き込み
f.write('test')
# closeメソッドでファイルを閉じる
f.close()

# もう一度文字列を書き換えて筆耕することによって内容が上書きされる
f = open('test.txt', 'w')
f.write('Test')
f.close()

# 追記する場合はモードを 'a' に指定する
# 読み込みは 'r'
f = open('test.txt', 'a')
f.write('Test')
f.close()

# ファイルに文字列を書き込むときは print関数を使うこともできる
# 引数に file=f のように書き込み先を指定する
f = open('test.txt', 'w')
f.write('Test\n')
print('I am print', file=f)
f.close()

# print関数の出力法
f = open('test.txt', 'w')
f.write('Test\n')
print('My','name', 'is', 'Mike',sep='#', end='!', file=f)
f.close()

# ファイルを使い終わったら閉じなければメモリを使ってしまう
# closeを忘れてしまう場合があるため with文を使う
# with文を使うことによって close を書く必要がないのでファイルを閉じ忘れることがないのでこちらが推奨されている
with open('test.txt', 'w') as f:
    f.write('Test')

# 複数行の改行
s = """\
AAA
BBB
CCC
DDD
"""

"""
windows の場合は改行コードが2文字分になるため、複数行の文字列をファイルに書き込む際に
newline='\n' のように指定することで改行コードがラインフィード(LF)のファイルを作成する
"""
with open('test.txt', 'w', newline='\n') as f:
    f.write(s)

# ファイルの読み込み
with open('test.txt', 'r') as f:
    print(f.read())

# 一行ずつの読み込み
# ループ文の中で readlineメソッドを使い一行ずつ読み込む break でループを抜ける
with open('test.txt', 'r') as f:
    while True:
        line = f.readline()
        print(line)
        if not line:
            break

# 改行なしの一行ずつの読み込み
with open('test.txt', 'r') as f:
    while True:
        line = f.readline()
        print(line, end='')
        if not line:
            break

# チャンク(かたまり)ごとの読み込み
with open('test.txt', 'r') as f:
    while True:
        chunk = 2
        # readメソッドの引数を指定することによって文字数の指定ができる
        line = f.read(chunk)
        # 改行が1文字に計算されている
        print(line)
        if not line:
            break

# ファイル内の位置の移動
# tellメソッドを使うと、現在の位置がわかる
with open('test.txt', 'r') as f:
    # 0 なので一番最初の位置にいる
    print(f.tell())
    # 現在の位置から引数に指定した文字数だけが読み込まれる
    print(f.read(1))

# seekメソッドを使うことによって位置の移動ができる
with open('test.txt', 'r') as f:
    # 0から数えて5番目の文字に移動する
    f.seek(5)
    print(f.tell())
    print(f.read(1))

with open('test.txt', 'r') as f:
    f.seek(14)
    print(f.read(1))
    f.seek(15)
    print(f.read(1))
    # 戻ることも可能
    f.seek(5)
    print(f.read(1))

# 書き込みをした後に読み込もうとするとエラーが起こる
s = """\
AAA
BBB
CCC
DDD
"""
# モードを 'w+' にすることによって書き込みと読み込みができる
with open('test.txt', 'w+') as f:
    f.write(s)
    print(f.read())

with open('test.txt', 'w+') as f:
    f.write(s)
    f.seek(0)
    print(f.read())

# 'r+'モードにすることで読み込んだ後に書き込みができる
# ファイルが存在しないなどの理由で読み込みができない場合にはエラーが起こるので注意
with open('test.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)
