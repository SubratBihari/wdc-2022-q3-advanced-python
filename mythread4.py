#!/usr/bin/env python3

# future -- a proxy for an answer that will (eventually) come

import threading
import time
import random

from concurrent.futures import ThreadPoolExecutor, submit


def hello(n):
    print(f'{n} Hello!')
    print(f'{n} Goodbye!')


with ThreadPoolExecutor() as executor:
    for i in range(10):
        result = executor.submit(hello, args=(i,))


# if we call "join" on a thread object, we wait for it to finish
for one_thread in all_threads:
    one_thread.join()


print('Done!')
