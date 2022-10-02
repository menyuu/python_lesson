# スコープについて
"""
Test Test ##############################
"""
# グローバル変数とローカル変数
# グローバル変数
animal = 'cat'
print(animal)

def f():
    print(animal)

f()

# ローカル変数
# 関数内でグローバル変数と同じ変数に値を入れると？
"""
animal = 'cat'

def f():
    ローカル変数を定義する場合、同じ変数に値を代入しようとすると代入前に出力しようとしたらエラーになる
    print(animal)
    animal = 'dog'

f()
"""

animal = 'cat'
def f():
    animal = 'dog'
    print('after:', animal)

f()
print('global:', animal)

# 関数内からグローバル変数を書き換えたい場合は global をつけて宣言する
animal = 'cat'
def f():
    global animal
    animal = 'dog'
    print('after:', animal)

f()
print('global:', animal)

# 関数内のローカル変数を出力する場合 locals() という関数がある(辞書型)
def f():
    animal = 'dog'
    print('lobal:', locals())

f()

# ローカル変数を定義してない場合は空の辞書型を返す
def f():
    print('local:', locals())

f()

# グローバル変数の出力 global()
animal = 'cat'
# docstring スクリプトのトップに置く
print('global:', globals())

animal = 'cat'

def f():
    """Test func doc"""
    print(f.__name__)
    print(f.__doc__)

f()
print('global:', __name__)