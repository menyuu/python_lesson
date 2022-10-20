import logging
import queue
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)

# 例えばサーバーとクライアントが両方立ち上がっていないと実行できないようにする場合などに使う
def worker1(barrier):
    r = barrier.wait()
    logging.debug('num={}'.format(r))
    while True:
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')

def worker2(barrier):
    r = barrier.wait()
    logging.debug('num={}'.format(r))
    while True:
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')

if __name__ == '__main__':
    # 引数に指定した数のスレッドが立ち上がってないと処理が進まない
    barrier= threading.Barrier(2)
    t1 = threading.Thread(target=worker1, args=(barrier,))
    t2 = threading.Thread(target=worker2, args=(barrier,))
    t1.start()
    t2.start()