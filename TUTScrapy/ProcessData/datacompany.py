import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="Vanhuy@123",
    database="linktest"
)
mycursor = mydb.cursor()
import json
from pprint import pprint

with open('company-new.json') as f:
    data = json.load(f)

# convert data
# i = 0
# dictCompany = {}
# for company in data:
#     i = i + 1
#     company["email"] = "huylv" + str(i) + "@linkjob.cf"
#     company["password"] = "Vanhuy@123"
#     if 'website' not in company:
#         company["website"] = "http://"
#     dictCompany[company["name"]] = i
#     company["id"] = i
# pprint(data)
#
# with open('dictcompany.json', 'w', encoding='utf8') as outfile:
#     json.dump(dictCompany, outfile, ensure_ascii=False)
#
# with open('dataCompany.json', 'w', encoding='utf8') as outfile:
#     json.dump(data, outfile, ensure_ascii=False)


# insert company
with open('dictcompany.json', encoding='utf8') as f:
    dictCompany = json.load(f)

with open('dataCompany.json', encoding='utf8') as f:
    dataCompany = json.load(f)
# check
# # for company in dataCompany:
# #     n = 0
# #     if company["scale"] is None:
# #         n = n + 1
# #     print(n)

import requests

API_ENDPOINT = "http://localhost:3000/api/companies"
for company in dataCompany:
    data = {
        "idcompany": company["id"],
        "email": company["email"],
        "password": "huylv244",
        "name": company["name"],
        "activated": True,
        "address": company["address"],
        "about": company["about"],
        "benefits": "Mang đến nhân viên môi trường làm việc chuyên nnghiệp thân thiện.",
        "goal": "Trở thành công ty số 1 trong lĩnh vực định hướng",
        "mission": "Mang lại giá trị cho công đồng và xã hội",
        "created_at": "2018-12-01T05:58:23.864Z",
        "website": company["website"],
        "scale": company["scale"]
    }
    r = requests.post(url=API_ENDPOINT, data=data)
    pprint(r)
    # pprint(data)
    # pprint(data)
