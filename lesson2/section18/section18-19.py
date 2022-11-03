import json
import pprint

l = ['apple', 'orange', 'banana', 'peach', 'mango']
l.insert(0, l[:])
print(l)
# pprint を使うことで見やすくできる
pp = pprint.PrettyPrinter()
pp.pprint(l)
# インデントを入れることができる
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(l)
# 〇文字以内で表示
pp = pprint.PrettyPrinter(indent=4, width=40)
pp.pprint(l)
# 〇文字までできれいに表示
pp = pprint.PrettyPrinter(indent=4, width=40, compact=True)
pp.pprint(l)

l.insert(0, l[:])
l.insert(0, l[:])
l.insert(0, l[:])
pp = pprint.PrettyPrinter(indent=4, width=40, compact=True, depth=3)
pp.pprint(l)

d = {'a': 'A', 'b': 'B', 'c': {'x': {'y': 'Y'}}}
pp = pprint.PrettyPrinter(indent=4, width=40)
pp.pprint(d)

l = ['apple', 'orange', 'banana', 'peach', 'mango']
l.insert(0, l[:])
print(json.dumps(l, indent=4))

d = {'a': 'A', 'b': 'B', 'c': {'x': {'y': 'Y'}}}
print(json.dumps(d, indent=4))

# json ではタプルを表示できないのでリストになってしまう
t = (1, 2, 3)
print(json.dumps(t, indent=4))