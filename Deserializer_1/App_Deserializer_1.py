import requests
import json

data = {
    "Name": "Taimor",
    "Roll": 355,
    "Subject": "Parshi"
    }

json_data = json.dumps(data)

URL = r"http://127.0.0.1:8000/"
# headers = {'Content-Type': 'application/json'}
# R = requests.post(url=URL, data=json_data, headers=headers)


R = requests.post(url=URL, data=json_data)
response_content = R.json()  # Use text to get the response content as a string

print(response_content)
