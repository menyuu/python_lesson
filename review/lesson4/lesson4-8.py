# 例外処理
# エラーが発生した時に行う処理
# try-except文
l = [1, 2, 3]
i = 5
# try と except の間でエラーが発生した場合に except の処理を行う
try:
    l[i]
except:
    print("Don't worry")
# 最後まで処理が行われる
print('last')

# 特定のエラーが発生した場合に処理を実行することもできる
# except の後に特定のエラーを記述する
# IndexError
try:
    l[i]
except IndexError:
    print("Don't worry")

# as の後ろに変数名を書くことによってエラーの内容を格納することができる
try:
    l[i]
except IndexError as ex:
    # print(f"Don't worry: {ex}")
    print("Don't worry: {}".format(ex))
