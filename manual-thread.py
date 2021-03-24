import threading
from core import time_it, time_sleep


@time_it
def call_time_sleep_thread():
    """Manual method of using threads"""
    print('\nCalling starting function with threading')
    t1 = threading.Thread(target=time_sleep, args=[2])
    t2 = threading.Thread(target=time_sleep, args=[2])
    t1.start()
    t2.start()
    t1.join()
    t2.join()


@time_it
def call_multi_time_sleep_thread():
    """Created multi threads using manual thread method"""
    print('\nCalling starting function with threading')
    threads = []
    for _ in range(100):
        t = threading.Thread(target=time_sleep, args=[1])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
