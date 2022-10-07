# csvファイルへの書き込み
# 標準ライブラリの csv を使用する
import csv

# 'w'モードで open する
# windows で open すると改行モードが \r\n になってしまうので newline='' のように入れる
with open('test.csv', 'w', newline='') as csv_file:
    # ヘッダーとして fieldnames を作成する
    # DictWriter関数で第1引数に CSVファイル、第2引数にfieldnamesを渡す
    # Writeheaderメソッドを実行すると CSVファイルが作成され書き込まれる
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()
    # writerowメソッドを使うことで辞書型のデータを渡す
    writer.writerow({'Name': 'A', 'Count': '1'})
    writer.writerow({'Name': 'B', 'Count': '2'})

# csvファイルの読み込み
# 'r'モードで open して、DictReader関数の引数に csvファイルを渡す
# 読み込んだ内容を forループで表示する
import csv

with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])