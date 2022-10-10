"""Generates ranking model to write to CSV

TODO (y) Rewrite to DB instead of CSV
"""
# DB の代わりに CSV に書く
import collections
import csv
import os
import pathlib

RANKING_COLUMN_NAME = 'NAME'
RANKING_COLUMN_COUNT = 'COUNT'
RANKING_CSV_FILE_PATH = 'ranking.csv'

class CsvModel(object):
    """Base csv model"""
    # csv のベースモデル
    def __init__(self, csv_file):
        self.csv_file = csv_file
        # csv_file のパスが存在しなければ処理を行う
        if not os.path.exists(csv_file):
            # ファイルの作成をする
            pathlib.Path(csv_file).touch()

# CsvModel を継承する
class RankingModel(CsvModel):
    """Definition of class that generates ranking model to write to CSV"""
    # CSVに書き出すためのランキングモデルを生成するクラスの定義
    # 初期化の引数に csv_file を None にし、引数を取れるように * を使う
    def __init__(self, csv_file=None, *args, **kwargs):
        # csv_file がなければ処理を行う
        if not csv_file:
            # get_csv_file_pathメソッドを csv_file に代入する
            csv_file = self.get_csv_file_path()
        # super して引数を渡す
        super().__init__(csv_file, *args, **kwargs)
        # csv のカラムをセットする
        self.column = [RANKING_COLUMN_NAME, RANKING_COLUMN_COUNT]
        # 初期値が 0 の defaultdict型を作る
        self.data = collections.defaultdict(int)
        # load_dataメソッドを呼び出す
        self.load_data()

    def get_csv_file_path(self):
        """Set csv file path.

        Use csv path if set in setting, otherwise use default
        """
        # csvパスが設定されている場合はそれを使用し、設定されていない場合はデフォルトを使用する
        csv_file_path = None
        # 例外処理
        # settingモジュールをインポート
        try:
            import setting
            # setting の CSV_FILE_PATH がある場合
            if setting.CSV_FILE_PATH:
                csv_file_path = setting.CSV_FILE_PATH
        except ImportError:
            pass

        # csv_file_path がなければ RANKING_CSV_FILE_PATH を代入する
        if not csv_file_path:
            csv_file_path = RANKING_CSV_FILE_PATH
        # csv_file_path を返す
        return csv_file_path

    def load_data(self):
        """Load csv data

        Returns:
             dict: Returns ranking data of dict type.
             辞書型のランキングデータを返す
        """
        # ファイルの読み取りと書き込み
        with open(self.csv_file, 'r+') as csv_file:
            # csv の読み取り
            reader = csv.DictReader(csv_file)
            # for文で辞書型のキーと値を指定する
            for row in reader:
                # self.data のキー RANKING_COLUMN_NAME, バリュー int型の　RANKING_COLUMN_COUNT を指定
                self.data[row[RANKING_COLUMN_NAME]] = int(row[RANKING_COLUMN_COUNT])
        # 戻り値の型は辞書型
        return self.data

    def save(self):
        """Save data to csv file"""
        # TODO (y) Use locking mechanism for avoiding dead lock issue
        # ファイルの書き込みと読み取り
        # newline='' にすることで改行をしない
        with open(self.csv_file, 'w+', newline='') as csv_file:
            # csv への書き込むためのオブジェクトを作成
            writer = csv.DictWriter(csv_file, fieldnames=self.column)
            # csv の作成
            writer.writeheader()

            # for文で
            for name, count in self.data.items():
                writer.writerow({
                    RANKING_COLUMN_NAME: name,
                    RANKING_COLUMN_COUNT: count
                })

    # ランキング上位のデータの取得
    def get_most_popular(self, not_list=None):
        """Fetch the data of the top most ranking

        Args:
            リストにある名前を除外する
            not_list (list): Excludes the name on the list.

        Returns:
            str: Returns the data of the top most ranking
        """
        # リストが None であれば空のリストを代入する
        if not_list is None:
            not_list = []

        # self.data がなければ None を返す
        if not self.data:
            return None

        # バリュー(値)で並び替える(key=〇〇.get と reverse=True を使って降順にする)
        sorted_data = sorted(self.data, key=self.data.get, reverse=True)
        # for文で sorted_data に入った辞書型のデータを1つずつ処理する
        for name in sorted_data:
            # name に not_list が含まれていればスキップする
            if name in not_list:
                continue
            return name

    def increment(self, name):
        """Increase rank for the give name."""
        # csvにデータを追加する
        # 頭の文字を大文字にする(その他は小文字)
        self.data[name.title()] += 1
        self.save()