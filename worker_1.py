import redis
from typing import Any
import time

red = redis.StrictRedis(host='localhost',
                        port=6379,
                        db=0)

# sample product, it can be tensor, ndarray, ...
product = 100

def str_to_bool(s):
    if s == b'True':
        return True
    if s == b'False':
        return False
    else:
        raise ValueError

while True:

    # publish product to consumer
    if red.get("new_product_worker_1") is None:
        red.set("new_product_worker_1", str(False))
    is_used = not str_to_bool(red.get("new_product_worker_1"))
    if is_used:
        product += 1
        red.set("product_worker_1", product)
        # set product status to 
        red.set("new_product_worker_1", str(True))
        print("worker 1 has published product: {}".format(product))
        time.sleep(0.5)
