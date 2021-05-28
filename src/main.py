import os

import synapseclient

username = os.getenv("INPUT_USERNAME")
apikey = os.getenv("INPUT_APIKEY")
pat = os.getenv("INPUT_PAT")

if apikey == '' and pat is '':
    raise ValueError("Must specify pat or apikey")

if pat != '':
    syn = synapseclient.login(authToken=pat,
                              rememberMe=True)
else:
    syn = synapseclient.login(email=username,
                              apiKey=apikey,
                              rememberMe=True)
