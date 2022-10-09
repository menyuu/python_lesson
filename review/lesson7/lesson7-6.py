# 一時ファイル
# tempfileライブラリ
# TemporaryFile関数を使うことによってI/Oバッファ上に一時ファイルを作成してくれる
# 処理が終わったら自動的に削除
import tempfile

with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# 実際に一時ファイルを作成する場合(削除しない場合)
# NamedTemporaryFile関数を使い、引数に delete=False を指定する
# 一時ファイルを open で開いてから書き込む
import tempfile

with tempfile.NamedTemporaryFile(delete=False) as t:
    # 一時ファイル名の表示
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())
# 今回は不要なので削除している
import os
os.remove(t.name)


# 一時ディレクトリ
# 中でファイルを作成し圧縮することなどができる
import tempfile

with tempfile.TemporaryDirectory() as td:
    print(td)

# TemporaryDirectory の定義から mkdtemp で一時的なディレクトリが作成されていることがわかる
# mkdtemp を使用すると一時的なディレクトリが作成することができる
import tempfile

with tempfile.TemporaryDirectory() as td:
    print(td)

temp_dir = tempfile.mkdtemp()
print(temp_dir)

