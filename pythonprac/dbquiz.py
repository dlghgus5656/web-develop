from pymongo import MongoClient  # pymongo를 사용하겠습니다
client = MongoClient('localhost', 27017)  # 내 컴퓨터에서 지금 돌아가고 있는 mongoDB에 접속할 겁니다
db = client.dbsparta  # dbsparta라고 하는 DB 이름으로 접속할 겁니다.(이름 없으면 자동으로 생섬됨)

# movies 컬렉션에서 title가 매트릭스인것을 찾아라
same_movie = db.movies.find_one({'title': "매트릭스"})
same_star = same_movie["star"]  # same_movie에서 찾은것에 star값을 same_star에 저장하라

print(same_movie["star"])  # same_movie에서 찾은것에 star(평점)을 출력하라

# 모든 movies 컬렉션에 star이 same_star에 저장된 값과 같은것을 찾아서 movies에 저장하라
# find로 모든 값들을 찾을땐 앞에 list를 써줘야한다?
movies = list(db.movies.find({"star": same_star}))

# 리스트안에 딕셔너리들을 출력하는 경우 바로print로 출력하면 가로로 보기 어렵게 출력되기 때문에 아래와 같이 for문을 사용해서 세로로 보기 편하게 출력하는것이 좋다
for movie in movies:  # movies를 차례대로 반복하면서 movie에 넣어둬라
    print(movie["title"])  # 넣어둔 movie 안에 값들에 title만 출력하라


# movies안에 title': '매트릭스인것에 star을 0으로 수정하라
db.movies.update_one({'title': '매트릭스'}, {'$set': {'star': "0"}})
# star에서 "0"으로 하면 문자값0이고 그냥 0 으로 해두면 숫자 0으로 업데이트된다
