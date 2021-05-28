## About

Github Action to login to [Synapse](www.synapse.org).


## Usage
To authenticate against Synapse, passwords are not allowed.  There are a couple ways to authenticate against Synapse.  Learn more about authenticating into Synapse [here](https://help.synapse.org/docs/Managing-Your-Account.2055405596.html#ManagingYourAccount-Loggingin)

### API key

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

### Personal Access Token

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
        pat: ${{ secrets.SYNAPSE_PAT }}
```
