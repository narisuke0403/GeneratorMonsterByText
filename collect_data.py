import time
import requests
from bs4 import BeautifulSoup


def collect():
    url1 = "http://www.geocities.jp/hoppygeo/DQ1/DQ1monster.html"
    url2 = "http://www.geocities.jp/hoppygeo/DQ2/DQ2monster.html"
    url3 = "http://www.geocities.jp/hoppygeo/DQ3/DQ3monster.html"

    html1 = requests.get(url1)
    time.sleep(1)
    html2 = requests.get(url2)
    time.sleep(1)
    html3 = requests.get(url3)
    
