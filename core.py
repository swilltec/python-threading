"""This file contains the core functions that will be used 
through out the module"""

import time


def time_sleep(seconds):
    """This function is used to mock a time consuming task"""

    print(f'sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done sleeping')


def time_it(func):
    """Function for timing function excution"""

    start = time.perf_counter()
    func()
    end = time.perf_counter()
    print(f'Finished in {round(end - start, 2)} second \n')
