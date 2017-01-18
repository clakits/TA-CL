import login
import json
import requests.packages.urllib3

rc=login.login_sw_rc()
resp = rc.get('/sensors')

print json.dumps(resp.json(), indent=4, sort_keys=True)