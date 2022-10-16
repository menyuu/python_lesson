import mysql.connector

# 本来は必ずユーザー名とパスワードを入れる
# conn = mysql.connector.connect(
#     host='127.0.0.1', user='', password=''
# )
# cursor = conn.cursor()
# cursor.execute(
#     'CREATE DATABASE test_mysql_database'
# )
# cursor.close()
# conn.close()

# どのデータベースを使うか
conn = mysql.connector.connect(
    host='127.0.0.1',
    database='test_mysql_database', user = '', password = ''
)
cursor = conn.cursor()
# データベースの中にテーブルを作成する
# cursor.execute(
#     'CREATE TABLE persons('
#     'id int NOT NULL AUTO_INCREMENT,'
#     'name varchar(14) NOT NULL,'
#     'PRIMARY KEY(id))'
# )

# データの作成
cursor.execute(
    'INSERT INTO persons(name) values("Mike")'
)
conn.commit()

# テーブルの確認
cursor.execute('SELECT * FROM persons')
# for文で取り出して確認できる
for row in cursor:
    print(row)

# UPDATE や DELETE は sqlite と同じ構文で更新ができる
cursor.execute(
    'UPDATE persons set name = "Michel" WHERE name = "Mike"'
)
cursor.execute(
    'DELETE FROM persons WHERE name = "Mike"'
)
cursor.close()
conn.close()
