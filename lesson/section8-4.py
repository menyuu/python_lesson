import os
import pathlib
import glob
import shutil

# ファイルの操作

# 存在するかどうか
# print(os.path.exists('test.txt'))
# ファイルかどうかの確認
# print(os.path.isfile('test.txt'))
# ディレクトリかどうかの確認
# print(os.path.isdir('design'))

# 名前の変更
# os.rename('test.txt', 'renamed.txt')
# シムリンク(ショートカット)
# os.symlink('renamed.txt', 'symlink.txt')

# ディレクトリの作成
# os.mkdir('test_dir')
# ディレクトリの削除
# os.rmdir('test_dir')

# 空のファイルの作成
# pathlib.Path('empty.txt').touch()
# ファイルの削除
# os.remove('empty.txt')

# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# ディレクトリの中身の表示
# print(os.listdir('test_dir'))
# pathlib.Path('test_dir/test_dir2/empty.txt').touch()
# ファイルのコピー
# shutil.copy('test_dir/test_dir2/empty.txt',
#             'test_dir/test_dir2/empty2.txt')
# ディレクトリの中身の確認
# print(glob.glob('test_dir/test_dir2/*'))
# 中身があるディレクトリの削除(消したものが戻せないため注意が必要)
# shutil.rmtree('test_dir')

# 現在の位置
# print(os.getcwd())