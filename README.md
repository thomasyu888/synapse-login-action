## About

Github Action to login to [Synapse](www.synapse.org).


## Usage
To authenticate against Synapse, passwords are not allowed.
Please utilize the API key.

```
name: ci

on:
  push:
    branches: master

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
    - name: synapse login
      uses: thomasyu888/synapse-login-action@0.1
      with:
        username: ${{ secrets.SYNAPSE_USERNAME }}
        apikey: ${{ secrets.SYNAPSE_APIKEY }}
```
