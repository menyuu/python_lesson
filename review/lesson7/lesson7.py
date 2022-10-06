# ファイルの作成
# open関数にファイル名とモードを指定する
# 'w'モードは write(書き込み)モード
f = open('test.txt', 'w')
# writeメソッドで内容の書き込み
f.write('test')
# closeメソッドでファイルを閉じる
f.close()