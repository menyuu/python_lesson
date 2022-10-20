import logging
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)
# ロックなどはグルーバルにすることもできるが推奨されていない
# lock = threading.Lock()

# def worker1(d, lock):
#     logging.debug('start')
#     # release するまで次のスレッドが邪魔しなくなる
#     # lock.acquire()
#     # with を使うことで acquire と release を行うこともできる
#     with lock:
#         i = d['x']
#         # 両方 x: 1 になってしまう
#         time.sleep(5)
#         d['x'] = i + 1
#         logging.debug(d)
#         # 2度目のロックをするときは release していないので処理が止まってしまう
#         # release するには lock の定義時に RLock を渡す
#         with lock:
#             d['x'] = i + 1
#     # release して次の処理を行える
#     # lock.release()
#     logging.debug('end')

# def worker2(d, lock):
#     logging.debug('start')
#     lock.acquire()
#     i = d['x']
#     d['x'] = i + 1
#     logging.debug(d)
#     lock.release()
#     logging.debug('end')

def worker1(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')

def worker2(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')

def worker3(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')

if __name__ == '__main__':
    d = {'x': 0}
    # lock = threading.Lock()
    # ２度ロックする場合
    # lock = threading.RLock()

    # セマフォをすることでロックするスレッドの数を操作できる
    semaphore = threading.Semaphore(2)

    # lock も引数に渡す
    # t1 = threading.Thread(target=worker1, args=(d, lock))
    # t2 = threading.Thread(target=worker2, args=(d, lock))

    t1 = threading.Thread(target=worker1, args=(semaphore,))
    t2 = threading.Thread(target=worker1, args=(semaphore,))
    t3 = threading.Thread(target=worker1, args=(semaphore,))
    t1.start()
    t2.start()
    t3.start()