# doctest
class Cal(object):
    def add_num_and_double(self, x, y):
        # doctestは対話型シェルのように >>> を使ってテストをする
        # テストの結果が違う場合エラーが返る
        # 本格的なテストではなくやり方の例を出す
        """Add and double

        >>> c = Cal()
        >>> c.add_num_and_double(1, 1)
        4

        エラーが起こるものの中にエラーの内容を記述する
        ... は省略
        >>> c = Cal()
        >>> c.add_num_and_double('1', '1')
        Traceback (most recent call last):
        ...
        ValueError
        """
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result

if __name__ == '__main__':
    # doctest を行う場合にインポートする
    import doctest
    doctest.testmod()
