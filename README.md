# Django_Yahoo_Movies
##link: https://django-yahoo-movies.herokuapp.com/

## 環境設定

環境 python 3.8 
requirements.txt 有詳細的安裝套件
請先安裝 django 


## 目標
Yahoo電影的本週新片 https://movies.yahoo.com.tw/movie_thisweek.html
此Project 為 Django的一個 Demo 將其部屬到heroku


## 執行檔案/說明
### 網路爬蟲的部分
Crawler/crawler.py 裡使用簡單的 Beautifulsoup 爬下來的網站
資料內容有電影的 中文名稱/英文名稱/上映日期/期待度

### Database的部分
為Postgresql(heroku的部屬不能使用預設的的SQlite

###執行檔案
python manage.py runserver 即可啟用host
python manage.py migrate 則會將資料的schema建構
python crawler.py 即可將爬蟲爬進資料庫
