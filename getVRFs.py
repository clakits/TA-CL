import login
import json
import common
import requests.packages.urllib3

#https://your-cluster-name.io/openapi/v1/sensors
rc=login.login_sw_rc()
resp = rc.get('/vrfs')

print json.dumps(resp.json(), indent=4, sort_keys=True)

csv_result=common.json2csv(resp.json())