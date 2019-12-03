import requests
import json

url = "https://webhacking.kr/login.php?login"

#Read account.json
accounts = None
with open("account.json") as f:
    accounts = json.loads(f.read())

session =  requests.session()

response = session.post(url=url, data=accounts, verify=False)
print response.text

