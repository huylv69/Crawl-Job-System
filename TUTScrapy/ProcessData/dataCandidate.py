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

with open("../candidate-new.json") as f:
    data = json.load(f)
print(len(data ))
with open('dictcareer.json', encoding='utf8') as f:
    dictCareer = json.load(f)

# # insert company
# for company in dataCompany:
#    sqlCompany = "INSERT INTO company (idcompany, email, password, activated, name , address, about, website, scale) value (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#    pprint(company["about"])
#    mycursor.execute(sqlCompany, (company["id"],company["email"],company["password"],True,company["name"],company["address"], company["about"],company["website"],company["scale"]))
# mydb.commit()