# Unittest
import unittest

import calculation

# release_name = 'lesson'
release_name = 'lesson2'

# テストが実行される前と後に処理を行う setup と teardown
# unittest の TestCase を継承する
class CalTest(unittest.TestCase):
    # 毎回テスト前にオブジェクトを作成する
    def setUp(self):
        print('setup')
        self.cal = calculation.Cal()

    def tearDown(self):
        print('clean up')
        del self.cal

    # テストのスキップにはデコレーターを使う
    # @unittest.skip('skip!')
    # skipIf で条件を指定できるのでバージョンなどによってテストを付け加えることも可能
    @unittest.skipIf(release_name=='lesson', 'skip!!')
    # test_ 以降の名前は何でもよいが、最初の test_ はルールとしてこれにする
    def test_add_num_and_double(self):
        # cal = calculation.Cal()
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)

    # 例外処理のテスト
    def test_add_num_and_double_raise(self):
        # cal = calculation.Cal()
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')

# if __name__ == '__main__':
#     unittest.main()