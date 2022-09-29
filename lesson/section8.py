# ファイルの作成
s = """\
AAA
BBB
CCC
DDD
"""
# with open('test.txt', 'w') as f:
#     f.write(s)
    # print関数を使っても書き込める
    # print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
    # ファイルを開いたままだとメモリを使ってしまう
    # withステートメントだとクローズしてくれる
    # f.close()

# with open('test.txt','r') as f:
    # print(f.read())
    # while True:
    #     chunk = 2
    #     line = f.read(chunk)
    #     print(line)
    #     if not line:
    #         break
    # print(f.tell())
    # print(f.read(1))
    # f.seek(5)
    # print(f.read(1))
    # f.seek(14)
    # print(f.read(1))
    # f.seek(15)
    # print(f.read(1))
    # f.seek(5)
    # print(f.read(5))

# w+ で書き込み + 読み込み
# 書き込みモードになっているので注意が必要
with open('test.txt', 'w+') as f:
    f.write(s)
    # 書き込んだ後は最後のインデックスになるので最初に戻るための seek
    f.seek(0)
    print(f.read())

# 読み込みからの書き込みなので事前にファイルが存在しない場合はエラーを返す
# with open('test2.txt', 'r+') as f:
#     print(f.read())
#     f.seek(0)
#     f.write(s)