import time
import asyncio
import requests
import aiohttp
from bs4 import BeautifulSoup


async def download(queue_download:asyncio.Queue,queue_save:asyncio.Queue):
    while True:
        url,log_file = await queue_download.get()
        full_url = f"{url}/{log_file}"
        async with aiohttp.ClientSession() as session:
            async with session.get(full_url) as response:
                content = await response.text()
                d = {
                    "log_file":log_file,
                    "content":content
                }
                queue_save.put_nowait(d)
        queue_download.task_done()
                
                
                
async def save(queue_save:asyncio.Queue):
    while True:
        d = await queue_save.get()
        log_file = d['log_file']
        content = d['content']
        with open(log_file,'w') as f:
            f.write(content)
        queue_save.task_done()

async def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com"
    queue_download = asyncio.Queue()
    queue_save = asyncio.Queue()
    
    nb_download_workers = 10
    nb_save_workers = 10

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = soup.find_all("a")
    log_files = [a['href'].lstrip() for a in all_a if a['href'].endswith('.log')]

    tasks = []
    
    for i in range(nb_download_workers):
        t = asyncio.create_task(download(queue_download,queue_save))
        tasks.append(t)

    for i in range(nb_save_workers):
        t = asyncio.create_task(save(queue_save))
        tasks.append(t)
    
    for log_file in log_files:
        t = url,log_file
        queue_download.put_nowait(t)

    await queue_download.join()
    await queue_save.join()

    for t in tasks:
        t.cancel()

    end = time.perf_counter()    
    print(f"{end-start:.3}s") 
    
    
    
if __name__=='__main__':
    asyncio.run(main())