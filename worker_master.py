import redis
from typing import Any

red = redis.StrictRedis(host='localhost',
                        port=6379,
                        db=0)

queue = []

def str_to_bool(s):
    if s == b'True':
        return True
    if s == b'False':
        return False
    else:
        raise ValueError

while True:
    # check supplier product status
    is_new = str_to_bool(red.get("new_product_worker_1"))
    # print(is_new)
    if is_new:
        taken_product = red.get("product_worker_1")
        queue.append(taken_product)
        print("take product from worker 1, current queue: {}".format(queue))
        # set product status to false
        red.set("new_product_worker_1", str(False))

    # publish product to consumer
    if red.get("new_product_worker_2") is None:
        red.set("new_product_worker_2", str(False))
    is_used = not str_to_bool(red.get("new_product_worker_2"))
    if is_used:
        if len(queue) < 1:
            continue
        product = queue.pop(0)
        red.set("product_worker_2", product)
        print("publish product to worker 2, current queue: {}".format(queue))
        # set product status to 
        red.set("new_product_worker_2", str(True))