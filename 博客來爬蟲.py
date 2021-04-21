import sys
import requests
from bs4 import BeautifulSoup
URL="https://search.books.com.tw/search/query/key/{0}/cat/all"

def generate_search_url(url,keyword):
    url= url.format(keyword)
    return url

def get_resource(url):
    headers ={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) APPLWebKit/537.36 (KHTML,like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    
    return requests.get(url,headers=headers,verify=False)

def parse_html(r):
    if r.status_code==requests.codes.ok:
        r.encoding = "utf8"
        soup=BeautifulSoup(r.text,"lxml")
    else:
        print("error"+url)
        soup=None
    return soup

def web_scraping_bot(url):
    booklist=[]
    print("retrive data from interent...")
    soup = parse_html(get_resource(url))
    print(soup)

if __name__=="__main__":
    if len(sys.argv) >1:
        url = generate_search_url(URL,sys.argv[1])
        booklist= web_scraping_bot(url)
        for iteam in booklist:
            print(iteam)