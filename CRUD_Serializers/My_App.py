import requests

URL = 'http://127.0.0.1:8000/'


def Request_GET(URL):
    R = requests.get(url=URL)
    return R.json()

data = Request_GET(URL)
for student in data:
    print('id','Name','Roll','City')
    for k, v in student.items():
        print(k,v,end=' ')
    print()