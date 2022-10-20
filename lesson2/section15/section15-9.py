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
    return i * 2

if __name__ == '__main__':
    # t1 = multiprocessing.Process(target=worker1, args=(i,))
    with multiprocessing.Pool(3) as p:
        # r = p.map(worker1, [100, 200])
        # map_async で非同期にできる(非同期にしたらすぐに次の行の処理をする)
        # r = p.map_async(worker1, [100, 200])
        # イテレーターで処理できる
        r = p.imap(worker1, [100, 200])
        # 処理が完了してから下の処理を行う
        logging.debug('executed')
        # logging.debug(r)
        # logging.debug(r.get())
        logging.debug([i for i in r])
        # map を使うことにより、下記の処理を簡略的にする
        # p1 = p.apply_async(worker1, (100, ))
        # p2 = p.apply_async(worker1, (100,))
        # logging.debug('executed')
        # logging.debug(p1.get())
        # logging.debug(p2.get())