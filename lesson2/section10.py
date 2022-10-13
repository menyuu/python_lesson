# ; をつけない
# x = 1;
y = 2

# 文字数を 80文字までに収める
# 超える場合は改行する
x = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

# def test_func(x, y, z,
#               fewfseafergafdgtrey4wfgrgfhdffesffehfdvfvdsfsdfgdfhfsfaftgaw):
#     """
#
#     :param x:
#     :param y:
#     :param z:
#     :param fewfseafergafdgtrey4wfgrgfhdffesffehfdvfvdsfsdfgdfhfsfaftgaw:
#     :return:
#
#     80文字を超えるURLの場合は改行すると読み込まれなくなるので改行しなくてもよい
#     """
#     print('test')

# 必要のない()をつけない
if (x and y):
    print('test')
if x and y:
    print('test')

# python のインデントは4つ
if x and y:
    print('test')

    x = {
        'test': 'sss'
    }
    # 1行で記述する場合
    y = {'test': 'sss'}
    # カンマの後などに1文字空ける
    print(x, y)
    x = 100
    yyyyy = 200
    zzzzzzzzz = 300

# 関数の定義などには間に1行空ける
# クラスの定義などの大きなものの間には2行空ける
# class Test(object):
#
#     def __init__(self, name='test'):
#         self.name = name
#
#     def test(self):
#         print('test')
#
#
# class Test2(Test):
#
#     def __init__(self, name):
#         super().__init__(name)
#
#     def test2(self):
#         print('testtest')

# 代入された変数の連結
word = 'hello'
word2 = '!'

# format を使うとわかりにくいので、+ で連結させる
new_word = '{}{}'.format(word,word2)
new_word = word + word2

# 間に文字列などを入れる場合は format を使うと見やすい
new_word = '{} aaaiiiuuu {}'.format(word,word2)

# ループを使った文字列の連結
# メモリの管理上ループで文字連結するより、append させたリストを join で文字列にするほうが良い
long_word = ''
for word in ['aaa', 'iiiii', 'uuuuuuuuu']:
    long_word += '{}eeeeeeooooo'.format(word)
print(long_word)

long_word = []
for word in ['aaa', 'iiiii', 'uuuuuuuuu']:
    long_word.append('{}eeeeeeooooo'.format(word))
new_long_word = ''.join(long_word)
print(new_long_word)

# シングルクォートかダブルクォートかは企業によって変わる
print('aaaaa')
print("aaaaa")

# 行数も企業によって変わる(ただし1行にすると見にくくなる)
if x:
    print('exit')
else:
    print('else')

if x: print('exit')
else:
    print('else')

# クラスの定義
# 最初が大文字
# キャラメルケース(単語同士を繋げるときに大文字にする)
# class RestaurantRobot(Robot):

# 関数や変数の定義
# スネークケース(単語同士をアンダーバーで繋げる)
# def recommend_restaurant(self):
# new_recommend_restaurant = self.ranking_model.get_most_popular()

# @property をつけるときは get をつけない
# @property
# def get_user_name(self):
#     return self.user_name

# @property
# def user_name(self):
#     return self._user_name

# グローバル変数は大文字にすることで明示的に書き換えをしないように示唆できる
# DEFAULT_ROBOT_NAME = 'Roboko'

# 実際に実行するファイルには
# def main():
#     main_program()
#
# if __name__ == '__main__':
#     main()
# のようにしてモジュールなどとしてインポートされても実行されないようにする