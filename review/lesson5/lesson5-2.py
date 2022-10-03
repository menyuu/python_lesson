# 組み込み関数
print(globals())

# sorted
ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

for key in ranking:
    print(key)

print(sorted(ranking))
# バリューで並べたい場合
print(sorted(ranking, key=ranking.get))
# getメソッドはキーを指定するとバリューを取得してくれる
print(ranking.get('A'))
# 降順に並び変える
print((sorted(ranking, key=ranking.get, reverse=True)))