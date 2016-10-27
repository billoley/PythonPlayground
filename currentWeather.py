import requests
import json
import datetime

url = 'http://api.openweathermap.org/data/2.5/weather?id=4352618&units=imperial&APPID=4b6e32316a64eee3fde1c8c1f629b8e6'

response = requests.get(url)
obj = json.loads(response.content)

print '{:20} {:20}'.format('city', obj.get('name'))

dt = obj.get('dt')
formattedDate = datetime.datetime.fromtimestamp(int(dt)).strftime('%Y-%m-%d %H:%M:%S')
print '{:20} {:20}'.format('date/time', formattedDate)

weatherMain = obj.get('weather')[0].get('main')
weatherDesc = obj.get('weather')[0].get('description')
print '{:20} {:20}'.format('weather', weatherMain + ' - ' + weatherDesc)

for l in obj.get('main'):
    print '{:20} {:19}'.format(l, str(int(obj.get('main').get(l))))

sunrise = obj.get('sys').get('sunrise')
sunriseStr = datetime.datetime.fromtimestamp(int(sunrise)).strftime('%H:%M:%S')
print '{:20} {:20}'.format('sunrise', sunriseStr)

sunset = obj.get('sys').get('sunset')
sunsetStr = datetime.datetime.fromtimestamp(int(sunset)).strftime('%H:%M:%S')
print '{:20} {:20}'.format('sunset', sunsetStr)

