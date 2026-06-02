import json
from pprint import pprint
content = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

f=open("data.json", "w")
json.dump(content, f,indent=2)
f.close()

f = open('data.json', 'r')
content = str(json.load(f))
print(json.loads(content))
f.close()