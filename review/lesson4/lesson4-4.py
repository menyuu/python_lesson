# lambda
# 短い関数を定義する場合に使う
# 複数個の簡単な処理などがあればより有効的になる
# 通常の関数
l = ['Mon', 'tue', 'wed', 'Thu', 'Fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

# 関数を引数として渡すときは関数名の後ろに()はつけない
change_words(l, sample_func)

# lambda
l = ['Mon', 'tue', 'wed', 'Thu', 'Fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# 1行で記述できる
# lambda のあとにある word が引数として後ろの処理に渡される
# lambda を使うと return を記述しなくて良いので簡潔に収まる
sample_func = lambda word: word.capitalize()
change_words(l, sample_func)

# lambda は 関数の引数に直接記述することも可能
change_words(l, lambda word: word.capitalize())