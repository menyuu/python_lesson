import threading
import multiprocessing

import concurrent.futures
import logging
import time

# 簡単な並列処理であれば concurrent.futures を使うと良い
logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')
# logging.basicConfig(level=logging.DEBUG, format='%(ProcessName)s: %(message)s')

def worker(x, y):
    logging.debug('start')
    r = x * y
    logging.debug(r)
    logging.debug('end')
    return r

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # multiprocess の場合以下で処理する
    # with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        # f1 = executor.submit(worker, 2, 5)
        # f2 = executor.submit(worker, 2, 5)
        # logging.debug(f1.result())
        # logging.debug(f2.result())

        # map を使うこともできる
        args = [[2, 2], [5, 5]]
        r = executor.map(worker, *args)
        # イテレーターで返ってくるため、forループなどで取り出す
        logging.debug(r)
        logging.debug([i for i in r])

if __name__ == '__main__':
    main()