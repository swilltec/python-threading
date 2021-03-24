from core import time_it, time_sleep


@time_it
def call_time_sleep_twice():
    print('Starting function with no threading')
    time_sleep(1)
    time_sleep(1)


@time_it
def call_multi_time_sleep():
    print('Starting function with no threading')
    for _ in range(10):
        time_sleep(1)
