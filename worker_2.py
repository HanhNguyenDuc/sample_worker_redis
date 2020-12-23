import redis
from typing import Any
import time

red = redis.StrictRedis(host='localhost',
                        port=6379,
                        db=0)

def str_to_bool(s):
    if s == b'True':
        return True
    if s == b'False':
        return False
    else:
        raise ValueError

while True:
    # check supplier product status
    is_new = str_to_bool(red.get("new_product_worker_2"))
    if is_new:
        taken_product = red.get("product_worker_2")
        print("taken product from master: {}".format(taken_product))
        # set product status to false
        red.set("new_product_worker_2", str(False))

        time.sleep(1)