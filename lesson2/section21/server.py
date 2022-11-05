import time

import zmq


context = zmq.Context()
# sock = context.socket(zmq.PUSH)
sock = context.socket(zmq.PUB)
sock.connect("tcp://127.0.0.1:5690")

id = 0
while True:
    id += 1
    sock.send(('sub1:' + str(id)).encode())
    print("Send: {}".format(id))
    time.sleep(1)