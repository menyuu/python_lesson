import base64
import os
import hashlib

# ハッシュは複合化できないようになっている
# print(hashlib.sha256(b'password').hexdigest())

user_name = 'user1'
user_pass = 'password'
db = {}

# クリプト系でよく使う
salt = base64.b64encode(os.urandom(32))
# print(salt)

# def get_digest(password):
#     password = bytes(password, 'utf-8')
#     # digest = hashlib.sha256(password).hexdigest()
#     digest = hashlib.sha256(salt + password).hexdigest()
#     # ストレッチング
#     for _ in range(10000):
#         digest = hashlib.sha256(bytes(digest, 'utf-8')).hexdigest()
#         print(digest)
#     # print(digest)
#     return digest

# hashlib のメソッドに get_digest のような処理を1回で行えるものがある
digest = hashlib.pbkdf2_hmac(
    'sha256', bytes(user_pass, 'utf-8'), salt, 10000
)

# db[user_name] = get_digest(user_pass)
# print(db)
db[user_name] = digest

def is_login(user_name, password):
    # return get_digest(password) == db[user_name]
    digest = hashlib.pbkdf2_hmac(
        'sha256', bytes(password, 'utf-8'), salt, 10000
    )
    return digest == db[user_name]

print(is_login(user_name, user_pass))