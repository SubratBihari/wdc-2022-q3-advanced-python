#!/usr/bin/env python3

import threading
import time
import random

def hello(n):
    
    print(f'{n} Hello!')


for i in range(10):
    # create a thread object, which will run hello
    t = threading.Thread(target=hello, args=(i,))  # args is a tuple

    # actually run the function in a new thread
    t.start()
