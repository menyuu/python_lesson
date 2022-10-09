# 時間について
# 標準ライブラリ datetime の使い方
import datetime

# now で現在の時刻を取得
now = datetime.datetime.now()
print(now)
# isoformat を使うと国際規格で定められた企画で表示できる
print(now.isoformat())

# strftime を使うと表示形式をある程度自分で設定できる
# strftime の引数に %d や %m, %y などで指定する
# %d 日付, %m 月, %y 年, %H 時間, %M 分, %S 秒, %f マイクロ秒
import datetime

now = datetime.datetime.now()
print(now.strftime('%d/%m/%y %H:%M:%S.%f'))
print(now.strftime('%Y-%m-%d %H:%M:%S.%f'))

# 年月日だけの取得は today で日付を取得し、isoformat で表示するか、strftime で日付のフォーマットにする
import datetime

today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))

# datetime.time で自分で好きな時刻を作成できる
t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H%M%S%f'))

# 時間の計算をしたいときは timedelta を使う
# 1週間前の時間を表示したい場合には、timedelta の引数に weeks=-1 を指定し、その返り値 d と時間を + で足し合わせる
import datetime

# 現在の時間を取得
now = datetime.datetime.now()
print(now)
# 1週間前の情報を取得
d = datetime.timedelta(weeks=-1)
print(d)
# 1週間前の日付を表示
print(now + d)

# 1年前の時間を確認する days=365 をして now - d を表示する
import datetime

now = datetime.datetime.now()
print(now)
d = datetime.timedelta(days=365)
print(d)
# 365日前の日付を表示
print(now - d)

# time をインポートして、time.sleep を実行すると指定した秒数後の処理を行う
import time

print('#####')
# 2秒後の次の処理を実行する
time.sleep(2)
print('#####')

# time.time() でエポックタイムを表示できる
# エポックタイム(1970年1月1日0時0分0秒)からの経過秒数を表示できる
import time
print(time.time())

# 時間を取得する処理はファイルのバックアップなどに使用できる
import os
import shutil
import datetime

now = datetime.datetime.now()

file_name = 'test.txt'

if os.path.exists('file_name'):
    shutil.copy(file_name, '{}.{}'.format(
        file_name, now.strftime('%Y_%m_%d_%H_%M_%S')))

with open(file_name, 'w') as f:
    f.write('test')