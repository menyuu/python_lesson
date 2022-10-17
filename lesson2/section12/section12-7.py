from neo4j import GraphDatabase


driver = GraphDatabase.driver(
    'bolt://localhost', auth=('neo4j', 'password')
)

# データベースの削除
def clear_db(tx):
    tx.run('MATCH (n) DETACH DELETE n')

def add_friend(tx, name, friend_name=None):
    if not friend_name:
        return tx.run(
            'CREATE (p:Person {name: $name}) RETURN p', name=name
        )
    return tx.run('MATCH (p:Person {name: $name})'
                  'CREATE (p)-[:FRIEND]->(:Person {name: $friend_name})',
                  name=name, friend_name=friend_name
                  )

def print_friend(tx, name):
    for record in tx.run(
            'MATCH (p {name: $name})-[:FRIEND]->(yourFriends)'
            'RETURN p, yourFriends', name=name
    ):
        print(record)

# 実行
with driver.session() as session:
    session.write_transaction(clear_db)
    session.write_transaction(add_friend, 'Tarou')
    for f in ['Mike', 'Nancy']:
        session.write_transaction(add_friend, 'Tarou', f)
    session.read_transaction(print_friend, 'Tarou')