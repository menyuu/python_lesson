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