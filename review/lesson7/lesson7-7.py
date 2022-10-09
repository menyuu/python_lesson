# Python でターミナルのコマンドを実行する
# 標準ライブラリ subprocess を使うとターミナル用のコマンドをPython上で実行できる
import subprocess

# run関数の引数にリストの中に実行したいコマンドを入れる
# Mac と Windows では異なるコマンドになるので注意
subprocess.run('dir', shell=True)

# shell=True の場合はエラーが返されてもプログラムが止まらない
import subprocess
# 存在しないコマンド
subprocess.run('diraaa', shell=True)
print('###')

r = subprocess.run('diraaa', shell=True)
# エラーコードの確認
print(r.returncode)

# check=True を指定すると Exception を発生させることができる
subprocess.run('diraaa', shell=True, check=True)
