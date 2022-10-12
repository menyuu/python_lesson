# ロボットモデルの定義
"""Defined a robot model"""

from interlude.roboter.models import ranking
from interlude.roboter.views import console

DEFAULT_ROBOT_NAME = 'Roboko'

# Robot ベースモデル
class Robot(object):
    """Base model for Robot."""

    # クラス変数の初期化とデフォルト引数
    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name='', speak_color='green'):
        self.name = name
        self.user_name = user_name
        self.speak_color = speak_color

    # オブジェクトメソッドの作成
    def hello(self):
        # ロボットとユーザーの会話を返す
        """Returns words to the user that the robot speaks at the beginning."""
        # break で抜けるまでループする
        while True:
            # views の console にある get_template の呼び出し
            # 引数に txtファイルと 出力時の文字色を渡す
            template = console.get_template('hello.txt', self.speak_color)
            # input関数で標準入力された値を user_name に代入する
            # input関数内で hello.txt を呼び出し $robot_name の部分には self.name(DEFAULT_ROBOT_NAME)
            user_name = input(template.substitute({'robot_name': self.name}))

            # 標準入力され user_name に代入されていれば名前の最初を大文字にして代入
            # ループを抜ける
            if user_name:
                self.user_name = user_name.title()
                break

# レストランモデルの呼び出し
# Robotモデルを継承する
class RestaurantRobot(Robot):
    """Handle data model on restaurant."""

    # クラスメソッドの初期化
    def __init__(self, name=DEFAULT_ROBOT_NAME):
        # super で初期化の継承
        super().__init__(name=name)
        # rankingモジュールにある RankingModel を代入する
        # 初期化でオブジェクトの作成
        self.ranking_model = ranking.RankingModel()

    # デコレーターの作成
    # 名前が入力されていないときに helloメソッドを呼び出すように指定
    def _hello_decorator(func):
        """Decorator to say a greeting if you are not greeting the user."""
        def wrapper(self):
            # user_name がなければ クラスメソッドの hello を呼び出す
            if not self.user_name:
                self.hello()
            # 引数に渡された func を返す
            return func(self)
        # wrapper関数を返す
        return wrapper

    # デコレーター
    @_hello_decorator
    # オススメのレストランの呼び出し
    def recommend_restaurant(self):
        """Show restaurant recommended restaurant to the user."""
        # rankingモジュールにある の get_most_popular を呼び出して代入する
        new_recommend_restaurant = self.ranking_model.get_most_popular()
        # new_recommend_restaurant がなければ None を返し、処理を終了する
        if not new_recommend_restaurant:
            return None

        # new_recommend_restaurant をリストにして代入する
        will_recommend_restaurants = [new_recommend_restaurant]
        # break で抜けだすまでループする
        while True:
            # greeting.txt を呼び出す
            # 第2引数に出力の色を渡す
            template = console.get_template('greeting.txt', self.speak_color)
            # 標準入力の呼び出した 'greeting.txt' を表示する
            # $ 部分には substitute を使い、引数に指定されたものをそれぞれ渡す
            is_yes = input(template.substitute({
                'robot_name': self.name,
                'user_name': self.user_name,
                'restaurant': new_recommend_restaurant
            }))

            # 標準入力された値を小文字にする
            # 入力された値が 'y' または 'yes' ならば break する
            if is_yes.lower() == 'y' or is_yes.lower() == 'yes':
                break

            # 入力された値が 'n' または 'no' ならば if文の処理を行う
            if is_yes.lower() == 'n' or is_yes.lower() == 'no':
                # rankingモジュールの ranking_model.get_most_popular を呼び出し代入
                # 引数の not_list に will_recommend_restaurants を代入する
                new_recommend_restaurant = self.ranking_model.get_most_popular(
                    not_list=will_recommend_restaurants
                )
                # new_recommend_restaurant が存在していればループを抜ける
                if not new_recommend_restaurant:
                    break
                # will_recommend_restaurants のリストに new_recommend_restaurant を入れる
                will_recommend_restaurants.append(new_recommend_restaurant)

    @_hello_decorator
    # ユーザーのお気に入りの店
    def ask_user_favorite(self):
        """Collect favorite restaurant information from users."""
        # break で抜けるまでループ
        while True:
            # templates からの呼び出し
            template = console.get_template(
                'which_restaurant.txt', self.speak_color
            )
            # 標準入力の呼び出した 'which_restaurant.txt' を表示する
            # $ 部分には substitute を使い、引数に指定されたものをそれぞれ渡す
            restaurant = input(template.substitute({
                'robot_name': self.name,
                'user_name': self.user_name
            }))
            # 好きなレストランが入力されたら ranking モデルにある icrementメソッドを呼び出す
            # 好きなレストランが入力されたらループを抜ける
            if restaurant:
                self.ranking_model.increment(restaurant)
                break

    @_hello_decorator
    def thank_you(self):
        """Show words of appreciation to users."""
        # good_by.txt の呼び出し
        template = console.get_template('good_by.txt', self.speak_color)
        # print関数を使ってそのまま good_by.txt を表示する
        print(template.substitute({
            'robot_name': self.name,
            'user_name': self.user_name
        }))