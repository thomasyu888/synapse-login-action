import os

import synapseclient

username = os.getenv("INPUT_USERNAME")
apikey = os.getenv("INPUT_APIKEY")

syn = synapseclient.login(email=username,
                          apiKey=apikey,
                          rememberMe=True)
