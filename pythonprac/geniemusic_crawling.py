import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 사용하겠습니다
client = MongoClient('localhost', 27017)  # 내 컴퓨터에서 지금 돌아가고 있는 mongoDB에 접속할 겁니다
db = client.dbsparta  # dbsparta라고 하는 DB 이름으로 접속할 겁니다.(이름 없으면 자동으로 생섬됨)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# body-content > div.newest-list > div > table > tbody > tr:nth-child(1)
# body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
# body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
# body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
trs = soup.select("#body-content > div.newest-list > div > table > tbody > tr")
# print(trs)

for tr in trs:
    a_tag = tr.select_one("td.info > a.title.ellipsis")
    # print(a_tag)
    if a_tag is not None:
        # print(a_tag.text)
        rank = tr.select_one("td.number").text[0:2].strip()
        title = a_tag.text.strip()
        singer = tr.select_one("td.info > a.artist.ellipsis").text
        print(rank, title, singer)
    #     doc = {
    #         "rank": rank,
    #         "title": title,
    #         "star": star
    #     }
