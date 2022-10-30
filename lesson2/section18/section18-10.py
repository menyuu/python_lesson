import collections
import queue


q = queue.Queue()
# マルチメソッド環境で使う
lq = queue.LifoQueue()
l = []
# 高速処理ができる
d = collections.deque()

# 追加
for i in range(3):
    q.put(i)
    lq.put(i)
    l.append(i)
    d.append(i)

# 取り出し
# 下の3つはスタックしているように取り出している
# for _ in range(3):
#     print('FIFO queue = {}'.format(q.get()))
#     print('LIFO queue = {}'.format(lq.get()))
#     # print('list       = {}'.format(l.pop()))
#     # 最初から取り出す
#     print('list       = {}'.format(l.pop(0)))
#     # print('deque      = {}'.format(d.pop()))
#     print('deque      = {}'.format(d.popleft()))
#     print()

# deque はインデックスでアクセスできる()
# print(d[1])
# print(d[-1])

# ローテーション
print(d)
d.rotate()
print(d)
d.rotate()
print(d)
d.rotate()
print(d)

# extend で追加できる
print(d)
d.extendleft('x')
print(d)
d.extend('y')
print(d)

d.clear()
print(d)