import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "jk")
print("status code : ", response.status_code)
print("encoding : ", response.encoding)
print(response.json())