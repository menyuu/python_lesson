# 特殊メソッド
# __init__ のような前後をアンダースコア2個ずつで囲まれたメソッド
class Word(object):
    def __init__(self, text):
        self.text = text

    # 文字列表現を返すメソッド
    def __str__(self):
        return 'word!!!!!'

    # 変数の長さを返すメソッド
    def __len__(self):
        return len(self.text)

    # オブジェクトが足しあわされた時に実行されるメソッド
    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    # クラスが == で比較された場合、オブジェクトのidが異なるためFalseが返る
    # __eq__ メソッドを使うことによって文字列が同じかどうかなどの比較ができる
    def __eq__(self, word):
        return self.text.lower() == word.text.lower()


w = Word('test')
# __str__
print(w)
# __len__
print(len(w))
# __add__
w2 = Word('##########')
print(w + w2)
# __eq__
w3 = Word('test')
print(id(w))
print(id(w3))
print(w == w3)
