import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def f(num, arr):
    # タイプの確認
    logging.debug(num)
    num.value += 1.0
    logging.debug(arr)
    for i in range(len(arr)):
        arr[i] *= 2

if __name__ == '__main__':
    # 引数に渡すものには整数であれば i 浮動小数点であれば f を渡す
    num = multiprocessing.Value('f', 0.0)
    arr = multiprocessing.Array('i', [1, 2, 3, 4, 5])

    p1 = multiprocessing.Process(target=f, args=(num, arr))
    p2 = multiprocessing.Process(target=f, args=(num, arr))
    p1.start()
    p2.start()
    # join して待つ
    p1.join()
    p2.join()
    logging.debug(num.value)
    logging.debug(arr[:])

