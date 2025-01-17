import requests
from bs4 import BeautifulSoup
import time
import threading
import concurrent.futures


def download(url,log_file):
    url_file_name = f"{url}/{log_file}"
    print(url_file_name)
    response = requests.get(url_file_name)
    with open(log_file,'w') as f:
        f.write(response.text)

def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    all_a = soup.find_all("a")
    #region old
    # log_files = []
    # for a in all_a:
    #     if a['href'].endswith('.log'):
    #         log_files.append(a['href'])
    # print(log_files)
    #endregion
    log_files = [a['href'].lstrip() for a in all_a if a['href'].endswith('.log')]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download,[url]*len(log_files),log_files)
    
    
        
    end = time.perf_counter()    
    print(f"{end-start:.3}s")     
if __name__=='__main__':
    main()
    
