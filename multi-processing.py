import concurrent.futures as cf
import multiprocessing

from core import time_sleep, time_it

@time_it
def call_time_sleep_multiprocess():
    """Manual method of using multiprocess"""
    print('\nCalling starting function with threading')
    p1 = multiprocessing.Process(target=time_sleep, args=[2])
    p2 = multiprocessing.Process(target=time_sleep, args=[2])
    p1.start()
    p2.start()
    p1.join()
    p2.join()





@time_it
def call_multi_time_sleep_multiprocess():
    """Created multi multiprocesss using concurrent multiprocess method"""
    print('\nCalling starting function with multiprocessing')

    with cf.ProcessPoolExecutor() as excutor:
        results = [excutor.submit(time_sleep, 1) for _ in range(20)]