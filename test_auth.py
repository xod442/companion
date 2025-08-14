import requests
from pycentral import NewCentralBase
from utility.token_info import token_info
import json


global token_info

print(f"This is central_info: ")
print(token_info)
print('-----------------------------------------------------')
client = NewCentralBase(token_info=token_info)


print(client)
