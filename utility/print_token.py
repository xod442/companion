import requests
from token_info import token_info
import json


def auth():
    # Run this script from the command line to generate a token
    url = "https://sso.common.cloud.hpe.com/as/token.oauth2"

    payload = {
        "grant_type": "client_credentials",
        "client_id": token_info['new_central']['client_id'],
        "client_secret":token_info['new_central']['client_secret']
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded"
    }

    token = requests.post(url, data=payload, headers=headers)
    token = json.loads(token.text)

    print(token['access_token'])

if __name__ == '__main__':
    auth()
