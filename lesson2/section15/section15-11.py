import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def f(conn):
    # parent_conn から child_conn に送信する
    conn.send(['test'])
    time.sleep(5)
    # 処理の終了で close させている
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(parent_conn, ))
    p.start()
    # recv することで send 送られてきたものを受け取れる
    logging.debug(child_conn.recv())