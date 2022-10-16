import pickle


class T(object):

    def __init__(self, name):
        self.name = name


# Python の形のまま保存できる
data = {
    'a': [1, 2, 3],
    'b': ('test', 'test2'),
    'c': {'key': 'value'},
    'd': T('test')
}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('data.pickle', 'rb') as f:
    data_loaded = pickle.load(f)
    print(data_loaded)

    print('------------------------')

    print(data_loaded['b'])
    print(data_loaded['d'])

    # Python の型でそのまま入る
    print(type(data_loaded['a']))
    print(type(data_loaded['b']))
    print(type(data_loaded['c']))
    print(type(data_loaded['d']))