

import requests

response = requests.get("https://baidu.com/")
print(response.status_code)