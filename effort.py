'''
Created on Sep 27, 2017

@author: lauthjo
'''
import requests
from bs4 import BeautifulSoup

url = "http://localhost:8080/SQL%20GateWay/SQLGatewayServlet"
        
payload = "sqlStatement=select%20top%2010%20*%20from%20test"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
}

response = requests.request("POST", url, data=payload, headers=headers)
doc = BeautifulSoup(response.text,"html.parser")
#print(doc.prettify())
#print(doc.table.get_text())

print("\n-----------")

#for line in doc.table:
#    print(line)
    
for row in doc.table.findAll("tr"):
    if not row.find("b"):
        cells = row.find("td")
        print(cells.get_text())
                                                                                