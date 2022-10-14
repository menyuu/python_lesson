# ログレベルというものがある
# ロギング

"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import  logging
import logging.config

import logtest


# ロギングのログレベルの初期値は WARNING になっている
# logging.basicConfig(level=logging.INFO)
# ファイルへの出力方法
# logging.basicConfig(filename='test.log', level=logging.INFO)

# フォーマットの形を変更する
# 出力時のフォーマットが変更される
# % と s の間に(levelname)などを入れる
# formatter = '%(levelname)s:%(message)s'
# formatter = '%(asctime)s:%(message)s'
# logging.basicConfig(level=logging.INFO, format=formatter)


# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')

# logging.info('info {}'.format('test'))
# Python2 のころに使われてた手法でも書ける
# logging.info('info %s %s' % ('test', 'test2'))
# logging の場合のみ以下の書き方もできる
# logging.info('info %s %s','test', 'test2')

# ロガー
# logger でレベルを変えることができる
# main で logging を最初に設定してそれ以外には logger で設定する
# logging.info('info')

# logging を引き継ぐ
# __name__ を指定するようにする
# logger = logging.getLogger(__name__)
# logger = logging.getLogger('main')
# logger.info('from main')
# logger.setLevel(logging.DEBUG)
# logger.debug('debug')

# logtest.do_something()


# class NoPassFilter(logging.Filter):
    # filetrメソッドをオーバーライドする
    # def filter(self, record):
    #     log_message = record.getMessage()
        # True であればロギングする
        # return 'password' not in log_message

# logger = logging.getLogger(__name__)
# addFilter をオブジェクトにして渡す
# logger.addFilter(NoPassFilter())
# logger.info('from main')
# logger.info('from main password = "test"')

# コンフィグ
# ファイルの読み込み
# logging.config.fileConfig('logging.ini')
# 辞書型での読み込み
# logging.config.dictConfig({
#     'version': 1,
#     'formatters': {
#         'sampleFormatter': {
#             'format': 'format=%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
#         }
#     },
#     'handlers' : {
#         'sampleHandlers': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'sampleFormatter',
#             'level': logging.DEBUG
#         }
#     },
#     'root': {
#         'handlers': ['sampleHandlers'],
#         'level': logging.WARNING,
#     },
#     'loggers': {
#         'simpleExample': {
#             'handlers': ['sampleHandlers'],
#             'level': logging.DEBUG,
#             'propagate': 0
#         }
#     }
# })

# logger = logging.getLogger(__name__)
# logger = logging.getLogger('simpleExample')
#
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')

# ロギングの書き方
# トラブルが起こると困る場所には多くのロギングを書く
logger = logging.getLogger(__name__)

# そのまま出力する場合
logger.error('Api call is failed')

# キーバリューで各場合
# 解析ソフトなどで利用できるものがある
logger.error({
    'action': 'create',
    'status': 'fail',
    'message': 'Api call is faild'
})