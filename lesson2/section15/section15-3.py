import logging
import queue
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)

def worker1(queue):
    logging.debug('start')
    # リストのように入る
    # 入れるときファーストイン、取得するときファーストアウト
    # queue.put(100)
    # time.sleep(5)
    # queue.put(200)
    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        # queue でタスクを動かしたのを記録する？
        queue.task_done()
        print(queue.task_done)

    logging.debug('end')

# def worker2(queue):
    # logging.debug('start')
    # logging と print では出力方法が変わるので順番が変わる
    # print(queue.get())
    # logging.debug(queue.get())
    # logging.debug(queue.get())
    # logging.debug('end')

if __name__ == '__main__':
    queue = queue.Queue()
    # t1 = threading.Thread(target=worker1, args=(queue,))
    # t2 = threading.Thread(target=worker2, args=(queue,))
    # t1.start()
    # t2.start()
    for i in range(1000):
        queue.put(i)
    ts = []
    for _ in range(3):
        t = threading.Thread(target=worker1, args=(queue,))
        t.start()
        ts.append(t)
    logging.debug('tasks are not done')
    queue.join()
    logging.debug('tasks are done')

    for _ in range(len(ts)):
        queue.put(None)

    [t.join() for t in ts]