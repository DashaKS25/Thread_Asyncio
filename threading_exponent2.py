import time
from multiprocessing import Process
from threading import Thread

"""
Exponent function.
"""


def exponent_func(num):
    result = num ** 1000000
    return result


"""
Synchronous.
"""


def sync():
    start_time = time.time()
    for num in [2, 3, 5]:
        exponent_func(num)
    end_time = time.time()
    return end_time - start_time


"""
Threaded.
"""


def threaded():
    start_time = time.time()
    threads = []
    for num in [2, 3, 5]:
        thread = Thread(target=exponent_func, args=(num,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    return end_time - start_time


"""
Multiprocess.
"""


def multiprocess():
    start_time = time.time()
    processes = []
    for num in [2, 3, 5]:
        process = Process(target=exponent_func, args=(num,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    return end_time - start_time


if __name__ == "__main__":
    sync_time = sync()
    thread_time = threaded()
    process_time = multiprocess()

    print(f"Synchronous Time: {sync_time} seconds")
    print(f"Threaded Time: {thread_time} seconds")
    print(f"Multiprocess Time: {process_time} seconds")