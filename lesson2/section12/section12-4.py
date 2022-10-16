# Python の標準ライブラリのDB
import dbm


# データベースの作成は 'c'モードにする
# with dbm.open('cache', 'c') as db:
    # string型か byte型のみしか作成できない
    # db['key1'] = 'value1'
    # db['key2'] = 'value2'

with dbm.open('cache', 'r') as db:
    print(db.get('key1'))