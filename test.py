import json
import requests

# print ("Hello World!")

url = 'https://raw.githubusercontent.com/ikshaku/jenkins-python/main/test.json'

# with open('test.json') as f:
#    data = json.load(f)

resp = requests.get(url)
data = json.loads(resp.text)
print(data['name'])    
