import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm


# メモリ上のデータベースを使う
# echo=True にすることによって、実行履歴を出力することができる
engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)
# sqlite で実行する場合
# engine = sqlalchemy.create_engine('sqlite:///test_sqlite2', echo=True)
# mysql で実行する場合
# コネクターするために pymysql を読み込む
# engine = sqlalchemy.create_engine(
#     'mysql+pymysql://{user_name}:{password}@{db_host}/test_mysql_database2'
# )

# クラス名が長いためクラスを継承するための変数
Base = sqlalchemy.ext.declarative.declarative_base()

# クラス名：オブジェクトの作成は1つのデータなので単数形
class Person(Base):
    # テーブルの作成
    # テーブル名：データが複数入っているので複数形
    __tablename__ = 'persons'
    # カラムの作成
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    name = sqlalchemy.Column(
        sqlalchemy.String(14)
    )

Base.metadata.create_all(engine)

# データベースへのアクセス
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# データの作成
p1 = Person(name='Mike')
session.add(p1)
p2 = Person(name='Nancy')
session.add(p2)
p3 = Person(name='Jhon')
session.add(p3)
session.commit()

# データの更新
# filter_by で特定する
p4 = session.query(Person).filter_by(name='Mike').first()
# データの代入
p4.name = 'Michel'
session.add(p4)
session.commit()

# データの削除
p5 = session.query(Person).filter_by(name='Nancy').first()
session.delete(p5)
session.commit()

# データベースの読み込み
persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)