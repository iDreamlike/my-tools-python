import requests


# headers = {"Content-Type": "application/json",
#            "Postman-Token": "fe824de0-c78b-430f-8ad5-f5104f41b919",
#            "User-Agent": "PostmanRuntime/7.43.0",
#            "Accept": "*/*",
#            "Host": "testlink.alfabank.ru",
#            "Accept-Encoding": "gzip, deflate, br",
#            "Connection": "keep-alive"
#            }
# cookies = {
#     "JSESSIONID": "11848A5B3BBF23CD19C6290CEA4EF9FD",
#     "SERVER_ID": "!9slRqH0+D3DA7jXx0gHPNyZdOveuXhZU5Vf8LonHo5CQ0c0POZBKSdUyUrAV9Uy4pmeABV6/20Njgw=="
# }
# data = {
#     "username": "corpApiUser",
#     "password": "1QAZxsw2"
# }

# response1 = requests.post("https://testlink.alfabank.ru/platform/create-user-corp/login", cookies = cookies, headers = headers, data = data)
# print(response1.status_code)
# print(response1.text)
# print(response1.headers.get("tokenforcreatingcorpuser"))

cookies = {
    "SERVER_ID": "!9slRqH0+D3DA7jXx0gHPNyZdOveuXhZU5Vf8LonHo5CQ0c0POZBKSdUyUrAV9Uy4pmeABV6/20Njgw=="
}

headers = {
    "TokenForCreatingCorpUser": "token token token"
    }
r = requests.get("https://testlink.alfabank.ru/platform/create-user-corp/create-basic-test-data", headers=headers, cookies=cookies)

print(r.status_code)
print(r.text)
