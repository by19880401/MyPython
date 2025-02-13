""" request demo"""

import requests

response = requests.get("https://baidu.com/")
print(f"status code: {response.status_code},{response.text}")
print("haha")
