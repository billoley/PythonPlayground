import requests
import json
import time

rangeInSec = 3600
now = int(time.time() * 1000)
host = ''
port = ''
url = host + ':' + port + '/api/query'

session = requests.Session();

headers = \
    {
        'Accepts' : 'text/json',
        'content-type' : 'application/json'
    }

payload = \
    {
        'msResolution' : 'true',
        'globalAnnotations' : 'true',
        'showQuery' : 'true',
        'start' : now - (rangeInSec * 1000),
        'end' : now,
        'queries' :
            [
                {
                    'metric' : 'statsd.tserver.QueueNumOps',
                    'aggregator' : 'count',
                    'downsample' : '30s-count',
                    'tags' :
                        {
                            'instance' : 'TabletServer',
                            'sampleType' : 'GAUGE'
                        }

                }
            ]
    }

response = session.post(url, headers=headers, data=json.dumps(payload), verify=False)

obj = json.loads(response.content)
print json.dumps(obj, indent=2)