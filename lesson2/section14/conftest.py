import os
import pytest

# 独自の fixture
# デコレーターで @pytest.fixture をすると独自の fixture になる
@pytest.fixture
# fixture の中に fixture を入れることができる
def csv_file(tmpdir):
    # return 'csv file!!!'
    # yield にすることでテストの前後の処理を入れられる
    with open(os.path.join(tmpdir, 'test.csv'), 'w+') as c:
        print('before test')
        # yield でテストが実行される
        yield c
        print('after test')

def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os name')