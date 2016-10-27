import json
import datetime


f = open('currentWeather.json', 'r')
data = f.read();
obj = json.loads(data)

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


