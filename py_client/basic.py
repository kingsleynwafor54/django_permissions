import requests



endpoint="http://localhost:8000/api/test/"

# get_response = requests.get(endpoint, params={"abc": 123}, json={"product":123})
# print(get_response.json())
# print(get_response.status_code)

get_response = requests.post(endpoint, params={"abc": 123}, json={'title':'Hello World',"content":123,"price":12345})
print(get_response.json())
print(get_response.status_code)

# get_response=requests.get(endpoint)

# print(get_response.json())