import requests
import json

url = 'http://api.openweathermap.org/data/2.5/forecast/city?id=4352618&units=imperial&APPID=4b6e32316a64eee3fde1c8c1f629b8e6'

response = requests.get(url)
obj = json.loads(response.content)
print json.dumps(obj, indent=2)


