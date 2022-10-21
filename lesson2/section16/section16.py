import string
import random

# 現在は変更されたため、エンコードする必要がある
from Crypto.Cipher import AES

# print(AES.block_size)
# print(string.ascii_letters)
key = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
).encode('utf-8')

# 初期ベクトル
iv = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
).encode('utf-8')
# print(key, iv)

# AES.MODE_CBC オープンSSLでも使われているアルゴリズム
# plaintext内の文字の長さは 16文字 * n のサイズでないとダメ
# plaintext = 'fgjwqufsagfdrfighjeroifu'.encode('utf-8')
# 読み込みとバイナリー型での書き込み
with open('plaintext', 'r') as f, open('enc.dat', 'wb') as e:
    plaintext = f.read().encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 16 * n にするには
    padding_length = AES.block_size - len(plaintext) % AES.block_size
    # 'fgjwqufsagfdrfighjeroifu' + '\x08\x08\x08\x08\x08\x08\x08\x08'
    plaintext += chr(padding_length).encode('utf-8') * padding_length
    cipher_text = cipher.encrypt(plaintext)
    print(cipher_text)
    e.write(cipher_text)

with open('enc.dat', 'rb') as f:
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = cipher2.decrypt(f.read())
    # decrypted_text = cipher2.decrypt(cipher_text)
    # print(decrypted_text)
    # print(decrypted_text[-1])
    # print(decrypted_text[:-decrypted_text[-1]])
    print(decrypted_text[:-decrypted_text[-1]].decode('utf-8'))
