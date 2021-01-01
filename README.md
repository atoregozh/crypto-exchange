## Setup

* Clone Git Repo

```bash
git clone https://github.com/atoregozh/crypto-exchange.git

cd crypto-exchange/
```

* Get Secrets: Create a text file called `secret.properties` in the repo root
and paste the contents of [this file](https://docs.google.com/document/d/1JCUCMkh4PxpWQzD2Erv6cWCFv2-CgEwqS82XpqsHDBA/edit). 
This file gets skipped in the .gitignore. This ensures we don't upload API keys or passwords unto github.

# Luno READ API credentials from Kesiena's account
luno_key_id = grk2h4dr99mhm
luno_secret = Xy_LPW_vvTXm9sjAHNH4fXX4WWErJcgLMqtcFCVcXxQ

* Install Python 3 & Pip 3:
```bash
brew install python3

pip3 install virtualenv
```

* Create & activate virtual env:
```bash
virtualenv -p python3 ./venv

source venv/bin/activate
```

* Install Python Dependencies:
```bash
pip install -r requirements.txt
```

## Run Code

Details coming soon



## Tear down

* Save python dependencies:
```bash

pip freeze > requirements.txt

```

* Git push

* Deactivate virtualenv:
```bash
deactivate
```


## API Keys

* 