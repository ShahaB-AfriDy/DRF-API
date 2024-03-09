
import requests

URL = "http://127.0.0.1:8000/"
R = requests.get(url=URL)
data = R.json()

print('\n')
print(data)
print('\nsuccessfully!!')