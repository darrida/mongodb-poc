import requests
import pprint
import json

data = {"name":"Ben Hammond",
        "email":"ema.il@gmail.com",
        "pwd":"12345.67890"}

res = requests.post('http://localhost:5000/create',
                    json=json.dumps(data))
print(res.status_code)
#pprint.pprint(res.json())

res = requests.get('http://localhost:5000/users')

print(res.status_code)
pprint.pprint(res.json())