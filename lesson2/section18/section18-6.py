import contextlib

def is_ok_job():
    try:
        print('do something')
        raise Exception('error')
        return True
    except Exception:
        return False

def clean_up():
    print('clean up')

def clean_up2():
    print('clean up2')

# try:
#     is_ok = is_ok_job()
#     print('more task')
# finally:
#     if not is_ok:
#         clean_up()

# 最後に呼び出すものをスタックできる？
with contextlib.ExitStack() as stack:
    # コールバック関数を入れることで最後に呼び出してくれる
    # 入れたものがスタックされるのであとから入れたものから順番に呼び出される
    stack.callback(clean_up)
    stack.callback(clean_up2)

    # デコレーターにすることによって直接書くこともできる
    @stack.callback
    def clean_up3():
        print('clean up3')

    is_ok = is_ok_job()
    print('more task')

    if is_ok:
        # スタックしているコールバック関数を取り除く
        stack.pop_all()
