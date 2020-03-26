import asyncio
import aiohttp
import time
import requests

URL = 'http://www.vk.com'


def sync_query():
    start_function_time = time.time()
    for i in range(0, 3):
        start_request_time = round(time.time(), 3)
        print(f'Starting request number {i} to {URL}')
        requests.get(URL)
        print(f'Request number {i} to {URL} took {round(time.time() - start_request_time, 3)}')
    print(f'All three requests to {URL} took {round(time.time() - start_function_time, 3)}')


print('\n------------------------------sync-----------------------------\n')
sync_query()


async def async_query(session, url, counter):
    start_request_time = round(time.time(), 3)
    print(f'Starting request number {counter} to {url}')
    async with session.get(url) as response:
        await response.text()
    print(f'Request number {counter} to {url} took {round(time.time() - start_request_time, 3)}')


async def async_caller(url, counter):
    async with aiohttp.ClientSession() as session:
        await async_query(session, url, counter)


loop = asyncio.get_event_loop()
tasks = []
for counter in range(3):
    task = asyncio.ensure_future(async_caller(URL, counter))
    tasks.append(task)

print('\n-----------------------------async------------------------------\n')
start_async_time = round(time.time(), 3)
loop.run_until_complete(asyncio.wait(tasks))
print(f'All thre requests to {URL} took {round(time.time() - start_async_time, 3)}')
