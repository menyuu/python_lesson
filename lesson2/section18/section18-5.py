import contextlib
import logging
import sys

# 標準入力
# x = input('Enter:')
# print(x)

# for line in sys.stdin:
#     print(line)

# 標準出力
# print('hello')
# sys.stdout.write('hello')

# エラー
# logging.error('Error!')
# sys.stderr.write('Error!')

# ファイルに書き込みたいといった場合にするリダイレクト先の変更
# with open('stdout.log', 'w') as f:
#     with contextlib.redirect_stdout(f):
        # print('hello')
        # help の書き込みなどもできる
        # help(sys.stdout)

with open('stdout.log', 'w') as f:
    with contextlib.redirect_stderr(f):
        logging.error('Error!')