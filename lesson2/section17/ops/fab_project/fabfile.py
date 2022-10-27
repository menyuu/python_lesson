from fabric.api import *
from fabric.colors import *
from fabric.contrib.files import *

# グローバル変数にすることによって臨機応変に対応できる
# パスの変更などをしたい場合に簡単に変えられるため
WEB_DIR = '/root/work'

env.hosts = ['root@172.16.200.101:22']
env.passwords = {'root@172.16.200.101:22': 'root'}
env.roledefs = {
    # どのようなものでも共通するものをインストールするように common を設定
    'common': ['root@172.16.200.101:22'],
    'web': ['root@172.16.200.101:22']
}

# 共通のパッケージのインストール
@task
@roles('common')
def install_packages():
    # -y で自動で yes と答える
    run('apt-get install -y software-properties-common')
    run('add-apt-repository universe')
    run('apt-get update')
    run('apt-get install -y python-setuptools')
    # easy_install は現在は非推奨になっているみたい...
    # run('easy_install pip')
    run('curl -o get-pip.py https://bootstrap.pypa.io/pip/2.7/get-pip.py')
    run('python get-pip.py')

@task
@roles('web')
def deploy_web():
    run('apt-get install -y supervisor')
    run('apt-get install -y gunicorn')
    run('pip install Flask==0.12.2')
    if not exists(WEB_DIR):
        run('mkdir {}'.format(WEB_DIR))

    put('roles/web/files/hello.py',
        '{}/hello.py'.format(WEB_DIR))
    put('roles/web/files/app.conf',
        '/etc/supervisor/conf.d/app.conf')
    run('service supervisor restart')


@task
def deploy_dev_server():
    install_packages()
    deploy_web()
    print(green('success'))