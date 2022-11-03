t = (1, 2, 3)
print('{0[0]}'.format(t))
print('{0[0]} {0[2]}'.format(t))
print('{i[0]} {i[2]}'.format(i=t))
# 下はコードが長くなる...
print('{} {}'.format(t[0], t[2]))
print('{0} {2}'.format(*t))
# 上と同じ
print('{0} {2}'.format(1, 2, 3))

d = {'name': 'taro', 'family': 'tanaka'}
print('{0[name]} {0[family]}'.format((d)))
print('{name} {family}'.format(**d))

# 左右に空白
print('{:<30}'.format('left'))
print('{:>30}'.format('right'))
print('{:^30}'.format('center'))
print('{0:^30}'.format('center'))
# 文字で囲む場合
print('{0:*^30}'.format('center'))
print('{name:*^30}'.format(name='center'))
print('{name:{fill}{align}{width}}'.format(
    name='center', fill='*', align='^', width=30))
print('{:,}'.format(123456789))
print('{:+f} {:+f}'.format(3.14, -3.14))
print('{:f} {:f}'.format(3.14, -3.14))
print('{:-f} {:-f}'.format(3.14, -3.14))
# 小数点第2位まで
print('{:.2%}'.format(19/ 22))
print('{}'.format(19/ 22))

# 整数、16進数、8進数、バイナリ
print(int(100), hex(100), oct(100), bin(100))
print('{0:d} {0:#x} {0:#o} {0:#b}'.format(100))
print('{0:d} {0:x} {0:o} {0:b}'.format(100))

for i in range(20):
    # バイナリ、整数、16進数(キャピタル)
    for base in 'bdX':
        # 5桁で表示
        print('{:5{base}}'.format(i, base=base), end=' ')
    print()