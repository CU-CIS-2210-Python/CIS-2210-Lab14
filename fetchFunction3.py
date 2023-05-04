import json
import requests #run "pip install requests" in the terminal!

r = requests.get("http://lab14.billkuker.com/data/squad.json")

print("breakpoint here")

print(r.headers['Content-Type'])

data = json.loads(r.text)

print(data['members'][1]['name'])