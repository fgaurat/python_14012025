import requests
from bs4 import BeautifulSoup
import time
def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    all_a = soup.find_all("a")
    # log_files = []
    # for a in all_a:
    #     if a['href'].endswith('.log'):
    #         log_files.append(a['href'])
    # print(log_files)
    log_files = [a['href'].lstrip() for a in all_a if a['href'].endswith('.log')]
    print(log_files)
    
    for log_file in log_files:
        url_file_name = f"{url}/{log_file}"
        print(url_file_name)
        response = requests.get(url_file_name)
        with open(log_file,'w') as f:
            f.write(response.text)
    end = time.perf_counter()    
    print(f"{end-start:.3}s")     
if __name__=='__main__':
    main()
