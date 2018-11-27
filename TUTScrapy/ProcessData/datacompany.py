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

with open('company.json') as f:
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



with open('dictcompany.json', encoding='utf8') as f:
    dictCompany = json.load(f)

with open('dataCompany.json', encoding='utf8') as f:
    dataCompany = json.load(f)



# # insert company
# for company in dataCompany:
#    sqlCompany = "INSERT INTO company (idcompany, email, password, activated, name , address, about, website, scale) value (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#    pprint(company["about"])
#    mycursor.execute(sqlCompany, (company["id"],company["email"],company["password"],True,company["name"],company["address"], company["about"],company["website"],company["scale"]))
# mydb.commit()


# pprint(dictCompany)
# pprint(data)
# pprint(data)
