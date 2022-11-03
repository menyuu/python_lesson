import enum


class Status(enum.Enum):
    # ステータスに数字を振り分ける
    # 別の名前のものでも最初に書いたものが返る
    ACTIVE = 1
    # 同じ値を違う名前にすることはできる
    RENAME_ACTIVE = 1
    INACTIVE = 2
    RUNNING = 3

print(Status.ACTIVE)
print(repr(Status.ACTIVE))
print(Status.ACTIVE.name)
print(Status.ACTIVE.value)

for s in Status:
    print(s)
    print(type(s))

print(Status(1))

print('######################')
# 別の名前のものでも最初に書いたものが返る
print(Status.ACTIVE)
print(Status.RENAME_ACTIVE)
print('######################')


# DB にサーバー情報を保存する
# string にするとメモリの消費が大きいので int で入れる
db = {
    'stack1': 1,
    'stack2': 2,
}

# グローバル変数で書くとあとから何が書いてたのかわからなくなる場合がある
# STATUS_ACTIVE = 1
# STATUS_INACTIVE = 2

# @enum.unique のデコレーターをつけることで同じ値を許可しなくできる
@enum.unique
class Status(enum.Enum):
    ACTIVE = 1
    # RENAME_ACTIVE = 1
    INACTIVE = 2
    RUNNING = 3

if Status(db['stack1']) == Status.ACTIVE:
    print('shutdouwn')
elif Status(db['stack2']) == Status.INACTIVE:
    print('terminate')

print(Status.ACTIVE)
print(type(Status.ACTIVE))
# オブジェクトかどうかの判定
print(Status.ACTIVE == 1)
print(Status.ACTIVE == Status(1))

print('######################')

# IntEnum にすることで数字を返す
class Status(enum.IntEnum):
    ACTIVE = 1
    INACTIVE = 2
    RUNNING = 3

print(Status.ACTIVE)
print(type(Status.ACTIVE))
# IntEnum にすることで Status.ACTIVE が 1 かどうかの判定
print(Status.ACTIVE == 1)

if db['stack1'] == Status.ACTIVE:
    print('shutdouwn')
elif db['stack2'] == Status.INACTIVE:
    print('terminate')


class Perm(enum.IntFlag):
    R = 4
    W = 2
    X = 1

print(Perm.R | Perm.W)
print(repr(Perm.R | Perm.W))
RWX = Perm.R | Perm.W | Perm.X
print(repr(RWX))
print(RWX)
print(type(RWX))
print(Perm.W in RWX)