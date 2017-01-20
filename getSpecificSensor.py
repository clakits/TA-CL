import login
import common
import json
import requests.packages.urllib3

#https://your-cluster-name.io/openapi/v1/sensors
rc=login.login_sw_rc()
resp = rc.get('/sensors')
#print dir(resp)
d1 = resp.json()

search_dict = {"platform": "CentOS-6.5"}
#search_dict = {"uuid": "9336a6252132d52b10711bb7c3e96f7043805bb8"}
#search_dict= {"host_name": "redhat7-00"}
result =common.search4match(d1, search_dict)
"""
if result.__len__():
    print json.dumps(result, indent=4, sort_keys=True)
else:
    print "NO match"
"""
csv_result=common.json2csv(result)