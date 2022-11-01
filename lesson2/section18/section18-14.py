# 正規表現
import re


# reコンパイル
# 高速化や再度同じコーディングなどを避ける
# 同じ正規表現を何度も使う場合は reコンパイルを使い記述したほうが良い
# 複数行に渡って書きたい場合は re.VERBOSE を使う
RE_STACK_ID = re.compile(
    r"""
    arn:aws:cloudformation:
    (?P<region>[\w-]+):         # region(このようにするとどの行に何があるかがすぐわかる)
    (?P<account_id>[\d]+)       # account_id
    :stack/
    (?P<stack_name>[\w-]+)/     # stack_name
    [\w-]+
    """, re.VERBOSE
)

s1 = ('arn:aws:cloudformation:us-east-2:123456789012:stack/'
     'mystack-mynestedstack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786')

s2 = ('arn:aws:cloudformation:us-east-1:123456789000:stack/'
     'mystack-mynestedstack-sggfrhxhum8y/f449b250-b969-11e0-a185-5081d0136786')

# raw_string な文字列を判断するために r を最初に入れている
# 数字などで桁数が決まっていれば桁数を入れてもよい
# (?P<名前>正規表現+) のように(?P<>)を使うことによってグループの名前を付けることができる
# 名前をつけたものは m.group(名前) とすることで取り出すことができる
for s in [s1, s2]:
    # m = re.match(
    #     (r'arn:aws:cloudformation:(?P<region>[\w-]+):(?P<account_id>[\d]+)'
    #     ':stack/(?P<stack_name>[\w-]+)/[\w-]+'), s
    # )
    m = RE_STACK_ID.match(s)

    if m:
        print('go next')
        print(m.group())
        print(m.group('region'))
        print(m.group('account_id'))
        print(m.group('stack_name'))
    else:
        raise Exception('Error')
    print(m)
    print()