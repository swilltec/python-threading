import concurrent.futures as cf

from core import time_it, time_sleep


@time_it
def call_multi_time_sleep_thread():
    """Created multi threads using concurrent thread method"""
    print('\nCalling starting function with threading')

    with cf.ThreadPoolExecutor() as excutor:
        results = [excutor.submit(time_sleep, 1) for _ in range(20)]