import requests
from pycentral.base import ArubaCentralBase
from utility.central_info import central_info
import json


global central_info

print(f"This is central_info: ")
print(central_info)
print('-----------------------------------------------------')
client = ArubaCentralBase(central_info=central_info)


print(client)
