import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

# pythonオブジェクトのように書けるが速度が遅い
# プロキシオブジェクト
def worker1(l, d, n):
    l.reverse()
    d['x'] += 1
    n.y += 1

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        l = manager.list()
        d = manager.dict()
        n = manager.Namespace()

        # 値を python のように代入できる
        l.append(1)
        l.append(2)
        l.append(3)
        d['x'] = 0
        # namespace はドット(.)をつけることで簡単に値を代入できる
        n.y = 0

        p1 = multiprocessing.Process(target=worker1, args=(l, d, n))
        p2 = multiprocessing.Process(target=worker1, args=(l, d, n))
        p1.start()
        p2.start()
        p1.join()
        p2.join()

        logging.debug(l)
        logging.debug(d)
        logging.debug(n)