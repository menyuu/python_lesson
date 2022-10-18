import os
class Cal(object):

    # 初期化やプロパティなどはテストしなくていい場合がある
    # def __init__(self, name='test'):
    #     self.name = name
    #
    # @property
    # def name(self):
    #     return self._name

    def add_num_and_double(self, x, y):
        if type(x) is not int or type(y) is not int:
            # if文がネストするとどこまでテストするかは企業などによる
            raise ValueError
        result = x + y
        result *= 2
        return result

    def save(self, dir_path, file_name):
        if not os.path.exists(dir_path):
            # テストを実行するときは if文の中身などもやらないとバグにつながる場合がある
            os.makedirs(dir_path)
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'w') as f:
            f.write('test')