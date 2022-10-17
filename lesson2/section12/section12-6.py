import datetime

# ドキュメント志向データベース
# json形式で記述
# ログ情報などを入れると便利
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']

stack1 = {
    'name': 'customer1',
    'pip': ['python', 'java', 'go'],
    'info': {'os': 'mac'},
    'date': datetime.datetime.utcnow()
}

stack2 = {
    'name': 'customer2',
    'pip': ['python', 'java'],
    'info': {'os': 'windows'},
    'date': datetime.datetime.utcnow()
}

# データベースの作成
db_stacks = db.staks
# stack_id = db_stacks.insert_one(stack1).inserted_id
# print(stack_id,type(stack_id))

# 中身の検索
# idから検索する場合は ObjectId で検索をしないと None が返る
# from bson.objectid import ObjectId
# str_stack_id= '634c5af83380d5dd1c89c943'
# print(db_stacks.find_one({'_id': ObjectId(str_stack_id)}))
# print(db_stacks.find_one({'name': 'customer1'}))
# print(db_stacks.find_one({'pip': ['python', 'java', 'go']}))
# Noneが返るもの
# print(db_stacks.find_one({'pip': []}))

# stack_id = db_stacks.insert_one(stack2).inserted_id
# print(stack_id, type(stack_id))

# すべて探す場合は for文で find関数を使う
# for stack in db_stacks.find():
#     print(stack)

# now = datetime.datetime.utcnow()
# 今より前の時間のものを取得
# for stack in db_stacks.find({'date': {'$lt': now}}):
#     print(stack)

# データの更新
# db_stacks.find_one_and_update(
#     {'name': 'customer1'},{'$set': {'name': 'test'}}
# )
# print(db_stacks.find_one({'name': 'test'}))

# データの削除
# db_stacks.delete_one({'name': 'test'})
# print(db_stacks.find_one({'name': 'test'}))