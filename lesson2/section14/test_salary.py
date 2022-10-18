import unittest
from unittest.mock import MagicMock
from unittest import mock

import salary


class TestSalary(unittest.TestCase):
    def test_calculation_salary(self):
        s = salary.Salary(year=2019)
        # MagicMock を用いて値を渡すことができる
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 101)
        # 呼ばれているかどうかを確認できる
        s.bonus_api.bonus_price.assert_called()
        # ループなどで不要に呼び出されていないかどうか(1回だけの呼び出しか)
        s.bonus_api.bonus_price.assert_called_once()
        # 引数に想定したものが渡されているかどうか
        s.bonus_api.bonus_price.assert_called_with(year=2019)
        # once と with の組み合わせ
        s.bonus_api.bonus_price.assert_called_once_with(year=2019)
        # 何回呼ばれたかの確認
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)

    def test_calculation_salary_no_salary(self):
        s = salary.Salary(year=2022)
        s.bonus_api.bonus_price = MagicMock(return_value=0)
        self.assertEqual(s.calculation_salary(), 100)
        # if文などで条件分岐して呼ばれてはいけないメソッドなどがある場合に使う
        s.bonus_api.bonus_price.assert_not_called()

    # mock で扱うことを明示的にする
    # デコレーターで書く場合
    # @mock.patch('salary.ThirdPartyBonusRestApi.bonus_price', return_value=1)
    @mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
    def test_calculation_salary_patch(self, mock_bonus):

        mock_bonus.return_value=1

        s = salary.Salary(year=2019)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        mock_bonus.assert_called()

    # with を使う場合
    # with のブロック内だけテストしたい時などに使う
    def test_calculation_salary_with(self):
        with mock.patch(
             'salary.ThirdPartyBonusRestApi.bonus_price'
        ) as mock_bonus:
            mock_bonus.return_value = 1

            s = salary.Salary(year=2019)
            salary_price = s.calculation_salary()

            self.assertEqual(salary_price, 101)
            mock_bonus.assert_called()

    # patcher にすることで setup や teardown で前後に処理を行える
    def setUp(self):
        self.patcher = mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
        self.mock_bonus = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_calculation_salary_patcher(self):
        self.mock_bonus.return_value = 1

        s = salary.Salary(year=2019)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        self.mock_bonus.assert_called()

    # 関数や例外処理を渡せる
    def test_calculation_salary_patch_side_effect(self):
        # 複雑な処理を作成して戻り値を渡せる
        # def f(year):
        #     return year * 2

        # side_effect メソッドを使う
        # self.mock_bonus.side_effect = f
        # self.mock_bonus.side_effect = lambda year: 1
        # 起こりうるエラーをテストすることで事前にソースコードを書き換えられる
        # self.mock_bonus.side_effect = ConnectionRefusedError
        # リストにすることもできる
        self.mock_bonus.side_effect = [
            1,
            2,
            3,
            ValueError('Bankrupt!!!')
        ]

        # s = salary.Salary(year=2019)
        # salary_price = s.calculation_salary()
        #
        # self.assertEqual(salary_price, 101)
        # self.assertEqual(salary_price, 100)
        # self.mock_bonus.assert_called()

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 101)
        s = salary.Salary(year=2018)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 102)
        s = salary.Salary(year=2019)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 103)
        s = salary.Salary(year=200)
        with self.assertRaises(ValueError):
            s.calculation_salary()

    # mock spec
    # spec=True にすることでクラスをモックとして認識してくれる
    # 下に書いたデコレーターが初めの引数になる
    @mock.patch('salary.ThirdPartyBonusRestApi', spec=True)
    @mock.patch('salary.Salary.get_from_boss')
    def test_calculation_salary_class(self, mock_boss, mock_rest):
    # 下記はオブジェクトの生成をわかりやすくしたイメージ(本来は上)
    # def test_calculation_salary_class(self, MockRest):
        mock_boss.return_value = 10
        mock_rest = mock_rest.return_value
        # mock_rest = MockRest.return_value
        # 下記は本来やり方と異なるので注意
        # 下記は mock オブジェクトの生成をわかりやすくしている
        # mock_rest = MockRest()
        # クラスメソッドを取得
        mock_rest.bonus_price.return_value = 1
        mock_rest.get_api_name.return_value = 'Money'

        s = salary.Salary(year=2019)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 111)
        mock_rest.bonus_price.assert_called()