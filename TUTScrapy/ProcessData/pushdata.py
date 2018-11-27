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
    listJob = json.load(f)
# pprint(data)

# Dict career
# sqlCareer = "select * from career"
# mycursor.execute(sqlCareer)
# myresult = mycursor.fetchall()
# pprint(myresult)
# dictCareer = {}
# for career in myresult:
#     dictCareer[career[1]] = career[0]
#     # pprint(career[0])
# pprint(dictCareer)
# with open('dictcareer.json', 'w', encoding='utf8') as outfile:
#     json.dump(dictCareer, outfile, ensure_ascii=False)


# insert address
# listAddress = set([])
# for job in data:
#     listAddress.add(job["address"][9:])
# # pprint(listAddress)
# for address in listAddress:
#     pprint(address)
#     sqlCareer = "INSERT INTO address (name) value (%s)"
#     mycursor.execute(sqlCareer, (address,))
# mydb.commit()

# insert career
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
# listURL = set([])
# for job in data:
#     listURL.add(job["url"])

    # pprint(job["career"])
# for company in listCompany:
#     pprint(len(listCompany))
# pprint(listURL)

# admin
# sqlAdmin = " insert into admin (username,password) value (%s,%s)"
# mycursor.execute(sqlAdmin, ("huylv", "pass"))
# mydb.commit()


# Company
# listCompany = set([])
# for job in data:
#     listCompany.add(job["company"])
#
# # pprint(len(listCompany))
# for company in listCompany:
#     pprint(len(listCompany))
# mydb.commit()



# insert job

from datetime import datetime
import time
with open('dictcompany.json', encoding='utf8') as f:
    dictCompany = json.load(f)

with open('dictcareer.json', encoding='utf8') as f:
    dictCareer = json.load(f)

for job in listJob:
    job["expired"] = job["expired"][:-1]+'9'
    # pprint(datetime.strptime(job["created"],'%d/%M/%Y'))
    if job["company"] not in dictCompany :
        continue
    if 'position' not in job:
        continue
    created  = datetime.strptime(job["created"], '%d/%m/%Y').strftime('%Y-%m-%d')
    expired  = datetime.strptime(job["expired"], '%d/%m/%Y').strftime('%Y-%m-%d')
    sqlJob = "INSERT INTO post (idcompany, idcareer,title,description,created,expired,category,require_skill,benefits,salary,address,contact,diploma,sex,experience,position) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sqlJob, (dictCompany[job["company"]],dictCareer[job["career"]],job["title"],job["description"],created,expired, job["category"],job["require_skill"],job["benefits"],job["salary"],job["address"],job["contact"],job["diploma"],job["sex"],job["experience"],job["position"]))
mydb.commit()
# pprint(listJob)