from pymongo import MongoClient  # pymongo를 사용하겠습니다
client = MongoClient('localhost', 27017)  # 내 컴퓨터에서 지금 돌아가고 있는 mongoDB에 접속할 겁니다
db = client.dbsparta  # dbsparta라고 하는 DB 이름으로 접속할 겁니다.(이름 없으면 자동으로 생섬됨)

# 코딩 시작
# insert/ find/ update/ delete 4가지 알면 됨

# doc = {'name': 'jane', 'age': 21}
# db.users.insert_one(doc)  # db안에 users라는 collection에 insert 해라


# db안에 users라는 collection에서 find해라 age가 21인 다만 _id 는 나타내지 말아라
# find로 모든 값들을 찾을땐 앞에 list를 써줘야한다?
# {'age': 21} 조건을 이렇게 줄수도있지만 조건을 주지 않을땐 그냥 {}로 냅두면 된다
# same_ages = list(db.users.find({'age': 21}, {'_id': False}))
# for person in same_ages:
#     print(person)


# find_one은 조건에 중복된 값이 있어도 단 하나만을 찾아온다
# user = db.users.find_one({'name': 'bobby'}, {'_id': False})
# print(user)


# name이 bobby인것을 찾아서 age를 19로 업데이트해라
# update_many는 조건에 맞는 모든것을 찾아서 업데이트를 해준다(위험해서 잘 쓰지 않는다_주로 update_one을 사용한다)
# db.users.update_one({'name': 'bobby'}, {'$set': {'age': 19}})


# # name이 bobby인것을 찾아서 삭제해라 이것도 마찬가지로 delete_many도 있지만 위와같은 이유로 잘 쓰지는 않는다
# db.users.delete_one({'name': 'bobby'})


# #################################간단 예시################################
# # 저장 - 예시
# doc = {'name': 'bobby', 'age': 21}
# db.users.insert_one(doc)

# # 한 개 찾기 - 예시
# user = db.users.find_one({'name': 'bobby'})

# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# same_ages = list(db.users.find({'age': 21}, {'_id': False}))

# # 바꾸기(업데이트) - 예시
# db.users.update_one({'name': 'bobby'}, {'$set': {'age': 19}})

# # 지우기 - 예시
# db.users.delete_one({'name': 'bobby'})
