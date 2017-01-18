from tetration import RestClient
def login_sw_rc():
    API_ENDPOINT = "https://marla.cisco.com"
    API_KEY      = "ace132ddef784667944f683cae6db28c"
    API_SECRET   = "0efcf4e825c8b899c5d93c625a7cd237014f1bb0"
    rc = RestClient(API_ENDPOINT, API_KEY, API_SECRET, verify=False)
    return rc
def login_hw_rc():
    API_ENDPOINT = "https://marla.cisco.com"
    API_KEY      = "6f30e0e3dc3549e5b00ffcd2f9fdb6d6"
    API_SECRET   = "9aa5181e9c3b91aa84b5413d0a2a5b0504579287"
    rc = RestClient(API_ENDPOINT, API_KEY, API_SECRET, verify=False)
    return rc

def login_flow_rc():
    API_ENDPOINT = "https://marla.cisco.com"
    API_KEY      = "76ad0edabbba46e29e997305afe2b42e"
    API_SECRET   = "2b117acf13440cdc07236c4d77260959be220611"
    rc = RestClient(API_ENDPOINT, API_KEY, API_SECRET, verify=False)
    return rc