import time
import aiohttp
import asyncio

async def get_sites(session, url, num_requests): #Here func which takes args
        start_time = time.time()#this str fixes the start time
        results = []#dic for results
        for _ in range(num_requests):#using  for loop, the specified number of requests to the  urls is executed
            response = await session.get(url)# Get request
            result = await response.text()#take response from urls
            results.append(result)#save answer
        return results, time.time() - start_time

async def main():
    urls = ["https://google.com", "https://amazon.com", "https://microsoft.com"]
    num_requests_per_site = 5
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[get_sites(session, url, 5) for url in urls])# do tasks(5 requests to urls) and save results
        print(f"results = {results}")


asyncio.run(main())


