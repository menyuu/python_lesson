import datetime

# 現在の時間
now = datetime.datetime.now()
print(now)
# 国際規格
print(now.isoformat())
print(now.strftime('%d/%m/%y-%H%M%S%f'))

# 年月日のみ
today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))

# 時間のみ
t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H_%M_%S_%f'))

# 過去の時間/未来の時間
print(now)
# d = datetime.timedelta(weeks=1)
d = datetime.timedelta(days=365)
print(now - d)

import time
# print('###')
# # 〇秒後まで処理を止める
# time.sleep(3)
# print('###')
# 1970.01.01からの秒数
print(time.time())

# ファイルのバックアップ
import os
import shutil

file_name = 'test.txt'

if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(
        file_name, now.strftime('%Y_%m_/%d_%H_%M_%S')))

with open(file_name, 'w') as f:
    f.write('test')