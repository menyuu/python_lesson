# ビット演算とシフト

# 論理和
print('論理和')
print(0 | 0)
print(0 | 1)
print(1 | 0)
# 1 が含まれていれば 1 になる
print(1 | 1)

# 論理積
print('論理積')
# 0 があれば 0 になる
print(0 & 0)
print(0 & 1)
print(1 & 0)
print(1 & 1)

# 排他的論理和
print('排他的論理和')
# 同じものであれば 0
print(0 ^ 0)
print(0 ^ 1)
print(1 ^ 0)
print(1 ^ 1)

# 反転
print('反転')
# ビットの反転
print(0)
print(~0)
print(1)
print(~1)
print(bin(0))
print(bin(~0))
print(bin(1))
print(bin(~1))
# ~ を 2個つけると元に戻る
print(bin(0))
print(bin(~~0))
print(bin(1))
print(bin(~~1))
print(bin(~~~0))
print(bin(~~~1))

# シフト
print('シフト')
print(bin(1 << 0))
print(bin(1 << 1))
print(bin(1 << 2))
print(bin(1 << 3))

print(1 * 2 * 2 * 2)
print(1 << 3)

print(bin(5))
print(bin(5 >> 1))
