# 今回はコードスタイルを無視して簡略的にコーディング
from fabric.api import run, env, roles, task

# ssh をターミナルから指定しなくてもよい
# ssh のポートは22番
env.hosts = ['root@172.16.200.101:22', 'root@172.16.200.102:22']
# passwordの設定
env.passwords = {
    'root@172.16.200.101:22': 'root',
    'root@172.16.200.102:22': 'root',
}
# ロール分けをすることができる
env.roledefs = {
    'web': ['root@172.16.200.101:22'],
    'db': ['root@172.16.200.102:22']
}

@roles('web')
def host_type():
    run('uname -s')

@roles('db')
def host_file():
    run('ls -al')

def all_files():
    run('ls -al')

# task のデコレーターを使うことによって明示的に利用する fabコマンドを限定できる
@task
def go():
    all_files()
    # run('ls -al')