import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="Vanhuy@123",
    database="linkjob"
)
mycursor = mydb.cursor()

import json
from pprint import pprint
with open('work-oke-2.json') as f:
    data = json.load(f)
# pprint(data)


# address
# listAddress = set([])
# for job in data:
#     listAddress.add(job["address"][9:])
# # pprint(listAddress)
# for address in listAddress:
#     pprint(address)
#     sqlCareer = "INSERT INTO address (name) value (%s)"
#     mycursor.execute(sqlCareer, (address,))
# mydb.commit()

# career
# listCareer = set([])
# for job in data:
#     listCareer.add(job["career"])
#     # pprint(job["career"])
# for career in listCareer:
#     pprint(career)
#     sqlCareer = "INSERT INTO career (name) value (%s)"
#     mycursor.execute(sqlCareer, (career,))
# mydb.commit()

#check url job
listURL = set([])
for job in data:
    listURL.add(job["url"])

    # pprint(job["career"])
# for company in listCompany:
#     pprint(len(listCompany))

pprint(listURL)

# admin
sqlAdmin = " insert into admin (username,password) value (%s,%s)"
mycursor.execute(sqlAdmin, ("huylv", "pass"))
mydb.commit()
# Company
# listCompany = set([])
# for job in data:
#     listCompany.add(job["company"])
#
# # pprint(len(listCompany))
# for company in listCompany:
#     pprint(len(listCompany))

# mydb.commit()



#



sql = "INSERT INTO post (idcompany, idcareer,title,description,created,expried,category,require_skill,benefits,salary,address,contact,diploma,sex,experience,position) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

# @app.route("/banner")
# def get_baner():
#     header = request.headers
#     if 'banner' in header:
#         con = MySQLdb.connect(host="192.168.23.191",  # your host, usually localhost
#                               user="huylv",  # your username
#                               passwd="G8kgph4GyIqiGhR7QCWE", #"G8kgph4GyIqiGhR7QCWE"; # your password
#                               db="email_marketing",
#                               charset='utf8')
#         url = str(header['banner']).strip()
#         query = con.cursor()
#         query.execute("SELECT banner_id FROM email_marketing.news_point_n where url ='" + url + "'")
#         banner_ids = []
#         for row in query.fetchall():
#             banner_ids.append(row[0])
#         query.close()
#         con.close()
#         data = dict()
#         data["list_banner"] = banner_ids
#         print(banner_ids)
#         return str(json.dumps(data, ensure_ascii=False))
#
#     else:
#         data = dict()
#         data["list_banner"] = []
#         return str(json.dumps(data, ensure_ascii=False))
