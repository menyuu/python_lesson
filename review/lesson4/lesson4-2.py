# 関数内関数
def outer(a, b):

    # 関数内関数
    # 関数の中で繰り返し行う処理がある場合に作成する
    def plus(c, d):
        return c + d

    # plusという関数に outer関数で受け取った引数 a と b を渡している
    r = plus(a, b)
    print(r)

outer(1, 2)

# クロージャー
# 関数内関数をクロージャーと呼ぶことがある
def outer(a, b):
    def inner():
        return a + b

    return inner

# 呼び出しただけだと inner関数のオブジェクトが返ってくるだけになる
print(outer(1, 2))
# 呼び出した関数を実行してはじめて関数内関数の結果が返ってくる
f = outer(1, 2)
r = f()
print(r)

# 外側の関数に渡す引数で、関数内関数の状態を変えることができる！
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

# 引数piに値を渡す
ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.14159)
print(ca1)
print(ca2)
# ca1 ca2 を実行すると外側の関数に渡した引数piの状態が関数内関数でも保持されている
# 変数の束縛(binding)
print(ca1(10))
print(ca2(10))
