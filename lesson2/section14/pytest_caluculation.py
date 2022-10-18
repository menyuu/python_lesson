# pytest
import os
import pytest

import calculation

is_release = True

# test_ をするとテストとして認識してくれる
# クラスにするときは継承しなく良い
# クラスの場合は最初に Test を入れる
class TestCal(object):

    # setup と teardown
    # class の setup と teardown でクラスを実行したときに呼び出される
    # setup_class teardown_class でメソッドを作成する
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()
        cls.test_dir = '/tmp/test_dir'
        # ファイルの作成
        cls.test_file_name = 'test.txt'

    # @classmethod
    def teardown_class(cls):
        # print('end')
        # del cls.cal
        # インポートは本来上でやるがわかりやすいように
        import shutil
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    # setup_method teardown_method でメソッドを作成する
    # 引数には method を渡す
    def setup_method(self, method):
        print('method={}'.format(method.__name__))
        # self.cal = calculation.Cal()

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
        # del self.cal

    def test_save_no_dir(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(self.test_dir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

    # pytest では conftest の pythonファイルがあれば優先して読み込む
    # fixture で受け取る
    # csv_file は独自の fixture
    def test_add_num_and_double(self, request, csv_file):
        print(csv_file)
        os_name = request.config.getoption('--os-name')
        print(os_name)
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        # cal = calculation.Cal()
        assert self.cal.add_num_and_double(1, 1) == 4

    # pytest でテストをスキップさせたい場合はデコレーターを使う
    # @pytest.mark.skip(reason='skip!')
    @pytest.mark.skipif(is_release==False, reason='skip!!')
    # 実行した結果が例外で返るかどうか
    # 例外でない場合はエラーで返る
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            # cal = calculation.Cal()
            self.cal.add_num_and_double('1', '1')
            # cal.add_num_and_double(1, 1)

    # pytest のテスト実行時にテンプディレクトリを作成してくれる
    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True
