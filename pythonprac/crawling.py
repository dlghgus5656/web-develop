from turtle import title
import requests
from bs4 import BeautifulSoup

# from pymongo import MongoClient  # pymongo를 사용하겠습니다
# client = MongoClient('localhost', 27017)  # 내 컴퓨터에서 지금 돌아가고 있는 mongoDB에 접속할 겁니다
# db = client.dbsparta  # dbsparta라고 하는 DB 이름으로 접속할 겁니다.(이름 없으면 자동으로 생섬됨)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작

trs = soup.select("#old_content > table > tbody > tr")

# old_content > table > tbody > tr:nth-child(2) > td.title > div > a
# old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
# old_content > table > tbody > tr:nth-child(2) > td.point

for tr in trs:
    a_tag = tr.select_one("td.title > div > a")
    # print(a_tag)
    if a_tag is not None:
        # print(a_tag.text)
        rank = tr.select_one("td:nth-child(1) > img")["alt"]
        title = a_tag.text
        star = tr.select_one("td.point").text
        # print(rank, title, star)
        doc = {
            "rank": rank,
            "title": title,
            "star": star
        }
        # db.movies.insert_one(doc)
