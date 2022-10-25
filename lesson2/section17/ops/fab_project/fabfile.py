# 今回はコードスタイルを無視して簡略的にコーディング
from fabric.api import run, env, roles, task, parallel, execute, runs_once

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

# fabコマンドで直接呼び出せない
def all_files():
    run('ls -al')

# task のデコレーターを使うことによって明示的に利用する fabコマンドを限定できる
@task
def go():
    all_files()
    # run('ls -al')

# taskデコレーターにdefault=True にすることで指定のない呼び出しをした場合に優先される
@task(default=True)
def who():
    run('whoami')

# parallelデコレーターをつけることでサーバーを同時に実行することができる
@task
@parallel(pool_size=2)
def para():
    run('ls -al')

# 引数を渡す場合 fab argtest:test1,test2 のような形で引数を渡す
@task
def argtest(arg1, arg2):
    print(arg1, arg2)

def test():
    return run('ls -al')

@task
def org():
    # メソッドを呼び出す場合は execute で呼び出す
    # testメソッドの戻り値をディクショナリ型で取得できる
    r = execute(test)
    print(r)

# 1回だけ実行したい場合 runs_once デコレーターを使う
@runs_once
def db_init():
    print('init')

@task
def deploy_db():
    db_init()
    db_init()