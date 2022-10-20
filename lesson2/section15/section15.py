import logging
import threading
import time


# logging を使って
logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)
# 並列化することで1つの処理が終わる前に並行して処理してくれる
def worker1(x, y=1):
    # print(threading.currentThread().getName(), 'start')
    logging.debug('start')
    logging.debug(x)
    logging.debug(y)
    time.sleep(5)
    # print(threading.currentThread().getName(), 'end')
    logging.debug('end')

# def worker2(x, y=1):
def worker2():
    # print(threading.currentThread().getName(), 'start')
    logging.debug('start')
    # logging.debug(x)
    # logging.debug(y)
    time.sleep(2)
    # print(threading.currentThread().getName(), 'end')
    logging.debug('end')

if __name__ == '__main__':
    # 指定した時間差で実行してくれる
    # 引数などに何を渡すかがわからないときは中身を見るかドキュメントを確認しに行こう
    t = threading.Timer(3, worker1, args=(100, ), kwargs={'y': 200})
    t.start()

    # スレッドをforループで回す
    # リストを作って入れなくてもよい
    # threads = []
    # for _ in range(5):
    #     t = threading.Thread(target=worker1)
    #     t.setDaemon(True)
    #     t.start()
        # threads.append(t)
    # enumerate を使うことでリストに入れなくても良い
    # print(threading.enumerate())
    # for thread in threading.enumerate():
    #     if thread is threading.currentThread():
    #         print(thread)
    #         continue
    #     thread.join()

    # t1 = threading.Thread(target=worker1)
    # 残っているスレッドを sleep を待たずにプログラムを強制終了する方法
    # t1.setDaemon(True)
    # t1 = threading.Thread(name='rename worker1', target=worker1)
    # 引数を渡すときはタプルにして渡す
    # t2 = threading.Thread(target=worker2)
    # t2 = threading.Thread(target=worker2, args=(100, ), kwargs={'y': 200})
    # t1.start()
    # t2.start()
    # print('started')
    # プログラムを強制終了させない方法
    # t1.join()
    # join されているのを明示的に書く場合もある
    # t2.join()