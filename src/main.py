import os

import synapseclient

username = os.getenv("INPUT_USERNAME")
apikey = os.getenv("INPUT_APIKEY")
pat = os.getenv("INPUT_PAT")

if apikey is None and pat is None:
    raise ValueError("Must specify pat or apikey")

if pat is not None:
    syn = synapseclient.login(authToken=pat,
                              rememberMe=True)
else:
    syn = synapseclient.login(email=username,
                              apiKey=apikey,
                              rememberMe=True)
