import asyncio
import sys
import time

"""
sys.set_int_max_str_digits(0)
This line sets the maximum number of digits in the string representation 
of integers to 0, which means there is no limit. 
This avoids errors when outputting very large numbers.
"""
sys.set_int_max_str_digits(0)

"""
async def calc_exponent
This is an asynchronous function that takes a number (num) and a degree exponent (exponent)
and computes num to the degree of exponent.
"""

async def calc_exponent(num, exponent):
    return num ** exponent


async def main():
    nums = [2, 3, 5]
    exponent = 1000000

    results_dict = {}

    for num in nums:
        result = await calc_exponent(num, exponent)
        results_dict[num] = result

    return results_dict

start_time = time.time() #this str fixes the start time
loop = asyncio.get_event_loop() #asyncio loop is created
results_dict = loop.run_until_complete(main()) # the main func starts and it's mean that execution is blocked until all asynchronous tasks are completed.
end_time = time.time() #fixes time of ending func runnig

print("2^1000000 =", results_dict[2])
print("3^1000000 =", results_dict[3])
print("5^1000000 =", results_dict[5])
print("Time runnig(seconds) :", end_time - start_time)#here prints result of func and time
