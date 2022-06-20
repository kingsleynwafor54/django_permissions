import requests
from getpass import getpass
 


auth_endpoint="http://localhost:8000/api/auth/"
password=getpass()
# endpoint="http://localhost:8000/api/products/detail/6"
# endpoint="http://localhost:8000/api/products/update/6"
# endpoint="http://localhost:8000/api/products/delete/6"
auth_response=requests.post(auth_endpoint,json={'username':'king1' ,"password":password})
print(auth_response.json())
print(auth_response.status_code) 

if auth_response.status_code == 200:
    token=auth_response.json()['token']
    headers = {  
        "Authorization": f"Token {token}"
    }
    endpoint="http://localhost:8000/api/products/"
    # endpoint="http://localhost:8000/api/products/detail/6"
    # endpoint="http://localhost:8000/api/products/update/6"
    # endpoint="http://localhost:8000/api/products/delete/6"
    get_response=requests.get(endpoint, headers=headers)
    print(get_response.json())
    print(get_response.status_code) 