import sqlite3

# conn = sqlite3.connect('test_sqlite.db')
# メモリー上にDBを作ってくれる
# 練習などには :memory: を使う
conn = sqlite3.connect(':memory:')

# テーブルの作成するには cursor が必要
curs = conn.cursor()

# テーブルの作成
# personsテーブル
# 主キー id
# カラム id name
curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
)
# データベースに保存する際は必ずコミットする
# コミットしなければ反映されない
conn.commit()

# データの保存
# INSERT INTO
curs.execute(
    'INSERT INTO persons(name) values("Mike")'
)
conn.commit()

curs.execute(
    'INSERT INTO persons(name) values("Nancy")'
)
curs.execute(
    'INSERT INTO persons(name) values("Jhon")'
)
conn.commit()

# UPDATE
curs.execute(
    'UPDATE persons set name = "Michel" WHERE name = "Mike"'
)
conn.commit()

# DELETE
curs.execute(
    'DELETE FROM persons WHERE name = "Michel"'
)
conn.commit()

curs.execute(
    'SELECT * FROM persons'
)
print(curs.fetchall())

# カーソルとコネクションをすべて close して終了する
curs.close()
conn.close()