import requests

BASE = "http://127.0.0.1:5000/"


response = requests.post(BASE + "video/1",{'views': 1000, "likes": 10})

print("POST")
print("Data : ",response.json())
print("Status code : ", response.status_code)
print("Encoding : " ,response.encoding)
print("Header : " , response.headers['content-type'])
print("---------------------")

input()

response = requests.get(BASE + "video/1")

print("GET")
print("Data : ",response.json())
print("Status code : ",response.status_code)
print("Encoding : ",response.encoding)
print("Headers : ",response.headers['content-type'])
print("End")