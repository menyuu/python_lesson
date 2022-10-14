# yaml
# スペース2個
# コンフィグ設定でよく使われる

"""
web_server:
  host: 127.0.0.1
  port: 80

web_server:
  host: 127.0.0.1
  port: 3306
"""
import yaml

with open('config.yml', 'w') as yaml_file:
    # 書き込みの際は第二引数に yaml_file を渡す
    # ブロックにする場合、さらに引数 default_flow_style=False を指定する
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': 3306
        }
    }, yaml_file, default_flow_style=False)

with open('config.yml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)
    print(data, type(data))
    print(data['web_server']['host'])
    print(data['web_server']['port'])
    print(data['db_server']['host'])
    print(data['db_server']['port'])