# ジェネレーター
# 復習(リストや辞書などを総称してイテレーター(反復可能なオブジェクト))
# ジェネレーターはイテレーターと同じく反復可能だが要素を取り出す度に要素を生成する
# リスト
l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

# ジェネレーター
# ジェネレーターには return がない代わりに yield を使う
# yield があることによってPythonがジェネレーターであると認識してくれる
def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

for g in greeting():
    print(g)

# ジェネレーターは next関数を使うことによってひとつずつ別の処理をはさみながら出力してくれる
# それ以上要素がない場合にはエラーが返る
g = greeting()
print(next(g))
print('---------------')
print(next(g))
print('---------------')
print(next(g))

def counter(num=10):
    for _ in range(num):
        yield 'run'

g = greeting()
c = counter()

# 複数の処理が間に入ってもジェネレーターは要素の状態を保持している
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

# 繰り返しなどの回数が多く一気に実行すると重くなる処理などで小分けするために使用する
# 関数が呼び出された場合 yield までの処理が実行される
# 再度 yield が呼び出されたら次の yield までの処理が実行され、処理が止まる
def greeting():
    yield 'Good morning'
    for i in range(100):
        print(i)
    yield 'Good afternoon'
    for i in range(100):
        print(i)
    print('test')
    yield 'Good night'

g = greeting()
print(next(g))
print(next(g))
print(next(g))