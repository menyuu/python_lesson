from review.lesson5.lesson_package.tools import utils
from ..tools import utils

def sing():
    return 'iosvutfwuwruwpvpowe'

# テスト用に書いていたつもりでもモジュールをインポートした時点で実行されてしまう
# __name__ が __main__ かどうかを判断する処理を入れる
if __name__ == '__main__':
    print(sing())
    print('animal:', __name__)

def cry():
    return utils.say_twice('gjklerjgajviwav:w')