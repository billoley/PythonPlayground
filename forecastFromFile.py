import json
import datetime


f = open('forecast.json', 'r')
data = f.read();
obj = json.loads(data)

print obj.get('city').get('name')
print

for w in obj.get('list'):
    dt = w.get('dt_txt')
    # formattedDate = datetime.datetime.fromtimestamp(int(dt)).strftime('%Y-%m-%d %H:%M:%S')
    min = str(int(w.get('main').get('temp')))
    weatherMain = w.get('weather')[0].get('main')
    weatherDesc = w.get('weather')[0].get('description')
    print dt + '\t\t' + min + '\t' + weatherMain + ' - ' + weatherDesc






