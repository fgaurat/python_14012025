import requests
from bs4 import BeautifulSoup
import time
import asyncio
import httpx
import aiohttp


async def download_and_save_aiohttp(url,log_file):
    full_url = f"{url}/{log_file}"
    async with aiohttp.ClientSession() as session:
        async with session.get(full_url) as response:
            content = await response.text()
            with open(log_file,'w') as f:
                f.write(content)
                
                
async def download_and_save_requests(url,log_file):
    full_url = f"{url}/{log_file}"

    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, requests.get, full_url)

    with open(log_file,'w') as f:
        f.write(response.text)

async def download_and_save_httpx(url,log_file):
    full_url = f"{url}/{log_file}"

    async with httpx.AsyncClient() as client:
        resp = await client.get(full_url)
        content = resp.text
        # write content to file_name
        with open(log_file,'w') as f:
            f.write(content)
            
                    
async def download(url,log_file):
    url_file_name = f"{url}/{log_file}"
    print(url_file_name)
    response = await requests.get(url_file_name)
    with open(log_file,'w') as f:
        f.write(response.text)

async def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    all_a = soup.find_all("a")

    log_files = [a['href'].lstrip() for a in all_a if a['href'].endswith('.log')]
    
    tasks = []

    for log_file in log_files:
        # tasks.append(download(url,log_file))
        # tasks.append(download_and_save_requests(url,log_file))
        # tasks.append(download_and_save_httpx(url,log_file))
        tasks.append(download_and_save_aiohttp(url,log_file))

    await asyncio.gather(*tasks)
        
    end = time.perf_counter()    
    print(f"{end-start:.3}s")     

if __name__=='__main__':
    asyncio.run(main())
    
    
