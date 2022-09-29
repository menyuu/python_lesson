# import tempfile
#
# # 使い終わると削除してくれる
# # 一時的なファイル
# with tempfile.SpooledTemporaryFile(mode='w+') as t:
#     t.write('hello')
#     t.seek(0)
#     print(t.read())
#
# # 実際に作成する
# with tempfile.NamedTemporaryFile(delete=False) as t:
#     print(t.name)
#     with open(t.name, 'w+') as f:
#         f.write('test\n')
#         f.seek(0)
#         print(f.read())
#
# # ディレクトリの作成
# with tempfile.TemporaryDirectory() as td:
#     print(td)
#
# temp_dir = tempfile.mkdtemp()
# print(temp_dir)