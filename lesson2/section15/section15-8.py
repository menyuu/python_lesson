import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)

def worker1(i):
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')
    return i

if __name__ == '__main__':
    # t1 = multiprocessing.Process(target=worker1, args=(i,))
    # 引数に渡したプールの数でワーカープロセスのコントロールする数を指定する
    with multiprocessing.Pool(3) as p:
        # 処理をブロック
        logging.debug(p.apply(worker1, (200, )))
        logging.debug('executed apply')
        # 処理の非同期
        p1 = p.apply_async(worker1, (100, ))
        p2 = p.apply_async(worker1, (100,))
        logging.debug('executed')
        logging.debug(p1.get())
        logging.debug(p2.get())