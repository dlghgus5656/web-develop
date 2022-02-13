# first_name = "hohyeon"
# last_name = "lee"
# num = str(2)

# print(first_name + num)


# def sum(num1, num2):
#     print("hi!")
#     return num1+num2


# result = sum(2, 3)

# print(result)


# def is_adult(age):
#     if age > 5:
#         print("성인입니다")

#     else:
#         print("청소년입니다")


# is_adult(5)
# is_adult(20)

# fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

# count = 0
# for ff in fruits:
#     print(ff)
#     if ff == "수박":
#         count += 1
# print(count)


# people = [{'name': 'bob', 'age': 20},
#           {'name': 'carry', 'age': 38},
#           {'name': 'john', 'age': 7},
#           {'name': 'smith', 'age': 17},
#           {'name': 'ben', 'age': 27}]

# for person in people:
#     print(person["name"], person["age"])
#     if person['age'] < 20:
#         print(person)

import requests  # requests 라이브러리 설치 필요

r = requests.get(
    'http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']

for gu in gus:
    gu_name = gu["MSRSTE_NM"]
    gu_mise = gu["IDEX_MVL"]
    if (gu_mise > 80):
        print(gu_name, gu_mise)
