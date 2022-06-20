import requests




endpoint="http://localhost:8000/api/products/"

get_response=requests.get(endpoint)#json={'title':'Hello World',"content":123,"price":12345})
print(get_response.json())
print(get_response.status_code)