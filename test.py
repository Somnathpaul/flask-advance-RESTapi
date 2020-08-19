import requests

BASE = "http://127.0.0.1:5000/"


response = requests.put(BASE + "video/1", {"likes": 10}, {"name": "python 3"},{"views": 1000}, {"dislikes": 0})
print(response.json())