s = 'aaaaaaaaaaa'\
    + 'bbbbbbbbbbbbb'
print(s)

x = (1 + 1 + 1 + 1 + 1 + 1 + 1
    + 1 + 1 + 1 + 1 + 1 + 1 + 1)
print(x)

"""
Pythonでは80文字以上入力すると次の行にいくようにする
\でも()でも同じ挙動
"""

x = 10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('10000000000000000000')
elif x == 10:
    print('10')
else:
    print('positive')

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

