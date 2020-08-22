import requests

BASE = "http://127.0.0.1:5000/"

data = [
        {'name': 'python tutorial','views': 1000, "likes": 10},
        {'name': 'ruby tutorial','views': 12, "likes": 1},
        {'name': 'nodejs tutorial','views': 150000, "likes": 198},
        {'name': 'c++ tutorial','views': 19798, "likes": 1}
       ]


for i  in range(len(data)):
    response = requests.post(BASE + "video/" + str(i),data[i])

    print("POST")
    print("Data : ",response.json())
    print("Status code : ", response.status_code)
    print("Encoding : " ,response.encoding)
    print("Header : " , response.headers['content-type'])
    print("---------------------")

input()

response = requests.get(BASE + "video/3")

print("GET")
print("Data : ",response.json())
print("Status code : ",response.status_code)
print("Encoding : ",response.encoding)
print("Headers : ",response.headers['content-type'])
print("---------------------")

input()

response = requests.delete(BASE + "video/2")

print("DELETE")
print("Data : ",response.json())
print("Status code : ",response.status_code)
print("Encoding : ",response.encoding)
print("Headers : ",response.headers['content-type'])
print("---------------------")

input()

response = requests.get(BASE + "video/2")

print("GET")
print("Data : ",response.json())
print("Status code : ",response.status_code)
print("Encoding : ",response.encoding)
print("Headers : ",response.headers['content-type'])
print("---------------------")

input()

response = requests.patch(BASE + "video/3",{'name':'c++'})

print("PATCH")
print("Data : ",response.json())
print("Status code : ",response.status_code)
print("Encoding : ",response.encoding)
print("Headers : ",response.headers['content-type'])
print("---------------------")

input()

response = requests.get(BASE + "video/3")

print("GET")
print("Data : ",response.json())
print("Status code : ",response.status_code)
print("Encoding : ",response.encoding)
print("Headers : ",response.headers['content-type'])
print("---------------------")