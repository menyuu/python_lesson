# memoizse
# 1度処理を実行したものを保存する
# キャッシュのような動作をする
# def memoize(f):
#     memo = {}
#     def _wrapper(n):
#         if n not in memo:
#             memo[n] = f (n)
#             print('hit')
#             print(memo)
#         return memo[n]
#     return _wrapper
#
# @memoize
# def long_func(n):
#     r = 0
#     for i in range(10000000):
#         r += n * i
#     return r
#
# for i in range(10):
#     # print(long_func(i))
#     long_func(i)
#
# print('next run')
# for i in range(10):
#     # print(long_func(i))
#     long_func(i)


# functools をインポートすることで上記と同じ処理をできる
import functools
# maxsize を指定することでキャッシュに保存する数を指定できる
# lru_cache は最近のキャッシュなので、maxsize で指定したものは後ろから数える
@functools.lru_cache(maxsize=5)
def long_func(n):
    r = 0
    for i in range(10000000):
        r += n * i
    return r

for i in range(10):
    print(long_func(i))

print(long_func.cache_info())

print('next run')
for i in range(10):
    print(long_func(i))

print(long_func.cache_info())
# clear することでキャッシュを消す
long_func.cache_clear()


print('more next run')
for i in reversed(range(10)):
    print(long_func(i))

print(long_func.cache_info())