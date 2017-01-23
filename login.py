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
    #API_KEY      = "76ad0edabbba46e29e997305afe2b42e"
    #API_SECRET   = "2b117acf13440cdc07236c4d77260959be220611"
    API_KEY = "655fa22032ca4a7ba0f56f0c9106f7e6"
    API_SECRET = "fb91bbc9633ee2c8513a7abb227e85fad75dd8ac"
    rc = RestClient(API_ENDPOINT, API_KEY, API_SECRET, verify=False)
    return rc

"""
def login_sw_rc():
    API_ENDPOINT = "https://ivana.cisco.com"
    API_KEY      = "743b0451345f4b4a817079ef0c7a3155"
    API_SECRET   = "88e57d63f2ea52657e632691b6a4976c0515066a"
    rc = RestClient(API_ENDPOINT, API_KEY, API_SECRET, verify=False)
    return rc
def login_hw_rc():
    API_ENDPOINT = "https://ivana.cisco.com"
    API_KEY      = "6f95919daa1d412db82fb32e624f9436"
    API_SECRET   = "e9e4afedecca592e563ed07609363a2ec4300d84"
    rc = RestClient(API_ENDPOINT, API_KEY, API_SECRET, verify=False)
    return rc

def login_flow_rc():
    API_ENDPOINT = "https://ivana.cisco.com"
    API_KEY      = "502d9384135342d9b517aefc27dace1b"
    API_SECRET   = "431f1ceb203dff4c7ac2cdde07c2415402eb12e6"
    rc = RestClient(API_ENDPOINT, API_KEY, API_SECRET, verify=False)
    return rc

"""