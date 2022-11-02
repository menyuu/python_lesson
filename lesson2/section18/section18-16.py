import re

# Greedy
s = '<html><head><title>Title</title></head></html>'

# html 部分のみをマッチさせたいが最初の < から最後の > がマッチしてしまう
print(re.match('<.*>', s))
# ? で 0回 か 1回をマッチさせる
print(re.match('<.*?>', s))