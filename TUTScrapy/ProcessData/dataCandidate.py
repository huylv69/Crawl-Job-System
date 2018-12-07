import mysql.connector
from random import randint

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="Vanhuy@123",
    database="linkjob"
)
mycursor = mydb.cursor()
import json
from pprint import pprint

# with open("../candidate-new.json") as f:
#     data = json.load(f)
# print(len(data))


# with open("uit_member.json") as f:
#     name = json.load(f)
# pprint(name[randint(0, 8790)]["full_name"])

# convert data candidate
# i = 0
# dictCompany = {}
# for candidate in data:
#     i = i + 1
#     candidate["email"] = "huylv" + str(i) + "@huylv.ga"
#     if 'language' not in candidate:
#         candidate["education"] = "Trình độ học vấn tốt \n"
#     else:
#         candidate["education"] = "Trình độ học vấn tốt \n Ngoại ngữ:" + candidate["language"]
#     candidate["skill"] = "Các kỹ năng cá nhân và nghề nghiệp tốt "
#     candidate["name"] = name[randint(0, 8790)]["full_name"]
#     candidate["id"] = i
#
# with open('datacandidate.json', 'w', encoding='utf8') as outfile:
#     json.dump(data, outfile, ensure_ascii=False)


with open('dictcareer.json', encoding='utf8') as f:
    dictCareer = json.load(f)

with open('datacandidate.json', encoding='utf8') as f:
    dataCandidate = json.load(f)
# Push data
import requests

API_ENDPOINT = "http://localhost:3000/api/students"
for candidate in dataCandidate:
    sex = candidate["sex"].lower() == "nam".lower()
    pprint(sex)
    if candidate["career"] not in dictCareer:
        continue
    else:
        idcareer = dictCareer[candidate["career"]]
    if 'objective' not in candidate:
        candidate["objective"] = "Mong muốn có điều kiện để làm việc, tích lũy kinh nghiệm trong công việc thực tiễn Trách nhiệm, nghiêm túc trong công việc sẽ đảm nhận Gắn bó lâu dài, có cơ hội thăng tiến trong công việc"

    if 'category' not in candidate:
        candidate["objective"] = "Khác"

    data = {
        "idstudent": candidate["id"],
        "email": candidate["email"],
        "name": candidate["name"],
        "password": "huylv244",
        "sex": sex,
        "address": candidate["address"],
        "birthday": "1996-04-24T19:16:42.528Z",
        "phone": "0985736902",
        "skill": candidate["skill"],
        "experience": candidate["experience"],
        "education": candidate["education"],
        "objective": candidate["objective"],
        "photo": "/api/containers/student/download/1544124866159_avatar.JPG",
        "other": "Tham gia nhiều hoạt động xã hội",
        "position": candidate["position"],
        "title": candidate["title"],
        "diploma": candidate["diploma"],
        "salary": candidate["salary"],
        "category": candidate["category"],
        "career": idcareer,
        "emailVerified": True
    }


    r = requests.post(url=API_ENDPOINT, json=data)
    pprint(r)

# # insert company
# for company in dataCompany:
#    sqlCompany = "INSERT INTO company (idcompany, email, password, activated, name , address, about, website, scale) value (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#    pprint(company["about"])
#    mycursor.execute(sqlCompany, (company["id"],company["email"],company["password"],True,company["name"],company["address"], company["about"],company["website"],company["scale"]))
# mydb.commit()
