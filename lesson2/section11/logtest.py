import logging

# logger をトップで読み込んで logger で設定する
logger = logging.getLogger(__name__)
# ログレベルを設定して main でも出力できるようにする
logger.setLevel(logging.DEBUG)
# ファイルへの出力
h = logging.FileHandler('logtest.log')
# logger しているものだけが渡される(今回だと下2つ)
logger.addHandler(h)

def do_something():
    # root になる
    logging.info('from logtest info')
    logger.info('from logtest')
    # main側でログレベルが違うと出力されない場合がある
    logger.debug('from logtest debug')