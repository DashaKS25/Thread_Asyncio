import time
from multiprocessing import Process
from threading import Thread

import requests

"""
 Function for executing a request to a site.
 """


def make_request(url, i):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    general_time = end_time - start_time
    print(f"Requests to {url} ended behind {general_time:.2f} seconds")


""" 
Function for five requests to the sites.
"""


def request_to_sites(url, i):
    print(f"Execution {i} requests to {url}:")
    for i in range(5):
        make_request(url, i)


"""
 Sync requests.
"""


def sync_request():
    print("Running sync requests")
    for url in ["https://google.com", "https://amazon.com", "https://microsoft.com"]:
        request_to_sites(url, 5)


"""
Threaded requests.
"""


def threaded_requests():
    print("Running threaded requests")
    threads = []
    for url in ["https://google.com", "https://amazon.com", "https://microsoft.com"]:
        thread = Thread(target=make_request, args=(url, 5))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


"""
Multiprocessed requests
"""


def multiprocessed_requests():
    print("Running multiprocessed requests")
    processes = []
    for url in ["https://google.com", "https://amazon.com", "https://microsoft.com"]:
        process = Process(target=make_request, args=(url, 5))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    sync_start_time = time.time()
    sync_request()
    sync_end_time = time.time()
    print(f"Time running sync requests: {sync_end_time - sync_start_time:.2f} seconds\n")

    threaded_start_time = time.time()
    threaded_requests()
    threaded_end_time = time.time()
    print(f"Time running threaded requests: {threaded_end_time - threaded_start_time:.2f} seconds\n")

    multiprocessed_start_time = time.time()
    multiprocessed_requests()
    multiprocessed_end_time = time.time()
    print(f"Time running multiprocessed requests: {multiprocessed_end_time - multiprocessed_start_time:.2f} seconds\n")
