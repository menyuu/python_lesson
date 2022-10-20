import logging
import multiprocessing


logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)

def worker1(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')

def worker2(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')

if __name__ == '__main__':
    i = 10
    t1 = multiprocessing.Process(target=worker1, args=(i,))
    t2 = multiprocessing.Process(name='rename worker2', target=worker2, args=(i,))
    t1.start()
    t2.start()