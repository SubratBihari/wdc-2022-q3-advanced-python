#!/usr/bin/env python3

# simple producer-consumer, with a queue

import threading
import time
import random
import queue

q = queue.Queue()


def hello(n):
    time.sleep(random.randint(0, 3))
    q.put(f'{n} Hello!')        # add something to the thread-safe queue
    q.put(f'{n} Goodbye!')


all_threads = []
for i in range(10):
    # create a thread object, which will run hello
    t = threading.Thread(target=hello, args=(i,))  # args is a tuple

    # keep track of this new thread
    all_threads.append(t)

    # actually run the function in a new thread
    t.start()

# if we call "join" on a thread object, we wait for it to finish
for one_thread in all_threads:
    one_thread.join()


print('Done!')

while not q.empty():
    print(q.get())              # retrieve from the thread-safe queue
