import login
import common
import json
# Flow Search
"""
req_payload = {
  "startTsIncl": "2017-01-20T09:00:00-0700",
  "endTsExcl": "2017-01-20T19:00:00-0700",
  "tenant": "Tetration",
  "vrf": "Tetration",
  "limit": 1000
}
"""
req_payload = {
  "startTsIncl": "2017-01-19T09:00:00-0700",
  "endTsExcl": "2017-01-20T19:00:00-0700",
  "tenant": "Default",
  "vrf": "Default",
  "filter": {"type": "eq", "field": "dst_port", "value": "53"}
}
rc = login.login_flow_rc()
print dir(rc)
resp = rc.post('/flowsearch', json_body=json.dumps(req_payload))
print json.dumps(req_payload)
#print json.dumps(resp.json(), indent=4, sort_keys=True)

