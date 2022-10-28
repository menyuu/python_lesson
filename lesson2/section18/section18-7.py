# io
# インメモリーストリーム
# ファイルを作成しなくてもメモリ上でファイルに読み書きしているようにできる
import io


# with open('/tmp/a.txt', 'w') as f:
#     f.write('test test')
#
# with open('/tmp/a.txt', 'r') as f:
#     print(f.read())

# テスト段階などに利用する
# ダウンロードした zip などを open する際などに使用できる
# f = io.StringIO()
f = io.BytesIO()
# f.write('string io test')
f.write(b'string io test')
f.seek(0)
print(f.read())
