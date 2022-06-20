import requests

 
product_id=input("What is the product id you want to use?\n")

try:
    product_id=int(product_id)
except:
    print(f"{product_id} not a valid id")

if product_id:   
    endpoint=f"http://localhost:8000/api/products/delete/{product_id}"
    get_response=requests.put(endpoint,json={'title':'Hello World My Old Friend' ,"price":1234})
    print(get_response.json())
    print(get_response.status_code) 