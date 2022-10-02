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

# NameError
del l
try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)

# Exception
# よくわからないエラーもキャッチしてくれる
# よくわからないエラーも全てキャッチし次のコードに進むのはあまり推奨されていないので注意
l = [1, 2, 3]
i = 5
try:
    () + 1
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other: {}'.format(ex))

# finally
# 最後に必ず処理してくれる
del l
try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other: {}'.format(ex))
finally:
    print('clean up')

# エラー処理されずにプログラムが中断した場合でも finally は実行される
# l = [1, 2, 3]
# i = 5
# try:
#     l[i]
# finally:
#     print('clean up')

# else
# エラーが発生しなかった場合にのみ実行される]
l = [1, 2, 3]
i = 5

try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
else:
    print("done")
finally:
    print('clean up')

# 独自例外
# raise を使うことによって例外を発生させることもできる
# raise IndexError('test error')

# エラーのクラスの作成
# Exception を継承する
class UppercaseError(Exception):
    # passにすることで Exception と同じ機能になる
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

# check()

# 独自に作ったエラーも try-except文にすることができる
try:
    check()
except UppercaseError as ex:
    print('This is my fault. Go next')

# 既存の例外を発生させることもできる
# 独自例外を作ることによって他のプログラマーにもわかりやすくなるので、あえてエラーを作成するのも有効
def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            # 既存の例外
            # 既存の例外を使用するより CheckFoodValueError といった名前の例外にすることによって他のプログラマーにもわかりやすくなる
            raise ValueError(word)

try:
    check()
except ValueError as ex:
    print('This is my fault. Go next')

# 関数を呼び出す側によって処理を返ることができるので、あえてエラーを書くこともある
# 例)自分のプログラムをサードパーティとして誰かに提供するときなど