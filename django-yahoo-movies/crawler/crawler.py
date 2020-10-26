import os
import sys


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


sys.path.append(PROJECT_DIR)
# Create your views here.
from bs4 import BeautifulSoup
import re
import time
import requests
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yahoo_movies.settings')
application = get_wsgi_application()
from movies.models import *
URL = "https://movies.yahoo.com.tw/movie_thisweek.html?page=1"

def generate_urls(url, start_page, end_page):
    urls = []
    for page in range(start_page, end_page+1):
        urls.append(url.format(page))
    return urls

def get_resource(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                "AppleWebKit/537.36 (KHTML, like Gecko)"
                "Chrome/63.0.3239.132 Safari/537/36"
    }
    return requests.get(url, headers=headers)
def format_date(date_str):
    pattern = '\d+-\d+-\d+'
    match = re.search(pattern, date_str)
    if match is None: 
        return date_str
    else: return match.group(0)

def get_movies(soup):
    movies = []
    rows = soup.find_all("div", class_="release_info_text")
    for row in rows:
        movie_name_div = row.find("div", class_="release_movie_name")
        cht_name = movie_name_div.a.text.strip()
        eng_name = movie_name_div.find("div", class_="en").a.text.strip()
        expectation = row.find("div", class_="leveltext").span.text.strip()
        photo = row.parent.find_previous_sibling("div", class_="release_foto")
        poster_url = photo.a.img["src"]
        release_date = format_date(row.find('div', 'release_movie_time').text)

        movies.append(Movies(
                cht_name = cht_name,
                eng_name = eng_name,
                expectation = expectation,
                poster_url = poster_url,
                release_date = release_date, 
            ))
    Movies.objects.bulk_create(movies)
    
def web_scraping_bot(urls):
    all_movies = []
    page = 1

    for url in urls:
        print("抓取: 第" + str(page) + "頁 網路資料中...")
        page = page + 1
        r = requests.get(url)
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text,'lxml')
            get_movies(soup)
            print("等待2秒鐘...")
            if soup.find("li", class_="nexttxt disabled"):
                break
            time.sleep(2)
        else:
            print("HTTP 請求錯誤")
      
    
     

urls = generate_urls(URL,1,1)
web_scraping_bot(urls)