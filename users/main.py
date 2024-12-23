import requests


payload = {"username": "corpApiUser", "password": "1QAZxsw2"}
headers = {"Content-Type": "application/json"}
r = requests.post("https://testlink.alfabank.ru/platform/create-user-corp/login", headers = headers, data = payload)

print(r.status_code)
print(r.text)
