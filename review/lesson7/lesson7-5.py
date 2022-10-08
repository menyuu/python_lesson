# tarファイルの作成
# Linux や Mac でよく使われている
# rarfileライブラリ
import tarfile

# with文でファイル名を指定して open する
# モードを 'w:gz' にする
with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')

# tarファイルの展開
# r:gzモード
# extractallメソッド
import tarfile

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    tr.extractall('test_dir')

# 中身の確認
import tarfile

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    with tr.extractfile('test_dir/sub_dir/sub_test.txt') as f:
        print(f.read())

# zipファイルの圧縮と展開
# zipfileライブラリ
# with文を書いて writeメソッドを使う
# zipファイルはディレクトリだけでなくその中身まで指定する必要がある
# ディレクトリのみを指定したら空のディレクトリが圧縮されるだけになる
import zipfile

with zipfile.ZipFile('test.zip', 'w') as z:
    z.write('test_dir')
    z.write('test_dir/test.txt')

# zipの確認
# globをインポートし一気にディレクトリやファイルを指定する
import zipfile
import glob

with zipfile.ZipFile('test.zip', 'w') as z:
    # アスタリスクを2つ付けることで recursive(再帰的)に確認できる
    for f in glob.glob('test_dir/**', recursive=True):
        print(f)
        z.write(f)

# zipファイルの展開
# extractall でディレクトリを指定して展開する
import zipfile
with zipfile.ZipFile('test.zip', 'r') as z:
    z.extractall('zzz2')

# zipファイルを展開せずに中身を確認
import zipfile

with zipfile.ZipFile('test.zip', 'r') as z:
    with z.open('test_dir/test.txt') as f:
        print(f.read())