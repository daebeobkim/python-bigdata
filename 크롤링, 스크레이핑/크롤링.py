import json, requests
from pandas.io.json import json_normalize

r = requests.get('http://rank.search.naver.com/rank.js')
json_normalize(json.loads(r.text), ['data', 'data'])