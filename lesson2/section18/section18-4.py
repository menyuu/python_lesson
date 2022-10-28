import contextlib
import os

try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass

# 行数が多いのをきれいにするには以下のように書く
with contextlib.suppress(FileNotFoundError):
    os.remove('somefile.tmp')