# import lesson_package.utils
from review.lesson5.lesson_package.tools import utils
# 相対パスで書く場合は現在の階層を探す必要があるのであまり推奨されていない
# from lesson_package.tools import utils
# 関数だけを import することもできるが、この場合どこから読み込まれたのかわからなくなってしまうので推奨されていない
# from lesson_package.utils import say_twice
# モジュール名が長い場合には as を使って省略してもよいが、こちらもあまり推奨されていない
# from lesson_package import utils as u

# r = lesson_package.utils.say_twice('hello')
r = utils.say_twice('hello')
# r = u.say_twice('hello')
print(r)

# from lesson_package.talk import human
# パッケージの中身を同時にインポートしたい場合は * で記述する
# * を使った読み込みはどんなモジュールが読み込まれているのかわからないためあまり推奨されていない
from lesson_package.talk import *

# print(human.sing())
# print(human.cry())

# * で読み込んだら __init__ に読み込みたいモジュール名を記述する必要がある
print(animal.sing())
print(animal.cry())

# ImportError が発生した場合の対処法
# try-except文を使う
# from lesson_package import utils の場所がすでに移動しているのでエラーが起こる
# バージョンによってファイルのパスが異なるといった場合に適応するために try-except文を書くことで回避できる
try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils