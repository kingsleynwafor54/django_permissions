import requests



endpoint="http://localhost:8000/api/products/"
# endpoint="http://localhost:8000/api/products/"

# get_response = requests.get(endpoint, params={"abc": 123}, json={"product":123})
# print(get_response.json())
# print(get_response.status_code)

data ={
    "title":"This field is done",
    "price":32.80
}

get_response = requests.post(endpoint, params={"abc": 123}, json=data)#json={'title':'Hello World',"content":123,"price":12345})

# get_response=requests.post(endpoint,json={'title':'Hello World',"content":123,"price":12345})
print(get_response.json())
print(get_response.status_code)

# get_response=requests.get(endpoint)

# print(get_response.json())