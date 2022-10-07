# 様々なファイル操作
# 標準ライブラリ os
# ecists を使うことでファイルが存在するかどうかを確認できる
import os

print(os.path.exists('test.txt'))

# isfile でファイルかどうかを確認
print(os.path.isfile('test.txt'))

# isdir でファイルかどうかを確認
print(os.path.isdir('design'))

# rename でファイル名の変更
# 第1引数に変更したいファイル名、第2引数に変更後のファイル名
# os.rename('test.txt', 'rename.txt')

# symlink
# windows のショートカットファイルのようなもの
# symlink で変更を行うと元のファイルも変更される
# os.symlink('rename.txt', 'symlink.txt')

# mkdir でディレクトリの作成
# os.mkdir('test_dir')

# rmdir でディレクトリの削除
# os.rmdir('test_dir')

# 標準ライブラリ pathlib
# touch 中身が空のファイルを作成できる
import pathlib
pathlib.Path('empty.txt').touch()

# remove でファイルの削除
import os

os.remove('empty.txt')

# listdir を使うとディレクトリの中にどのようなディレクトリがあるかを確認できる
import os

# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# 'test_dir' の中にどんなディレクトリがあるかを確認できる
print(os.listdir('test_dir'))

# globライブラリをインポートして glob関数を利用する
# ディレクトリの中にあるファイルを列挙するもの
import pathlib
import glob

pathlib.Path('test_dir/test_dir2/empty.txt').touch()
# 引数にアスタリスク( * )を使うことによって、ディレクトリの中に存在する全てのファイルを調べる
print(glob.glob('test_dir/test_dir2/*'))

# 高度なファイルの操作
# shutilライブラリをインポート
# copy でファイルをコピー
import shutil
import glob

# 第1引数にコピー元、第2引数にコピー先を指定する
shutil.copy('test_dir/test_dir2/empty.txt', 'test_dir/test_dir2/empty2.txt')
print(glob.glob('test_dir/test_dir2/*'))

# rmdir はディレクトリの中身が空の場合のみ削除できる
# rmtree で空でないディレクトリを削除
# ディレクトリを誤って指定してしまうと中身がすべて消えてしまうので注意
import shutil
shutil.rmtree('test_dir')