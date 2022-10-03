# スクリプトが読み込まれる時の注意点
print(__name__)

import config
# モジュールがインポートした際に config のモジュールにある print('config:', __name__) が読み込まれる
# インポートしたタイミングで print関数が読み込まれるのでモジュールに記述する際には注意が必要

print('lesson:', __name__)

import lesson_package.talk.animal

print('lesson', __name__)

# このファイルが他のファイルからも読み込まれる可能性がある(__main__ でなくなる可能性がある)
# 上記のことを防ぐために関数などで __main__ であれば実行するようにする
def main():
    lesson_package.talk.animal.sing()

if __name__ == '__main__':
    main()