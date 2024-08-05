import requests

response = requests.get('http://reqres.in/api/users?page=2')
print(response)  # Status code of the response
#print(response.json())  # JSON response content
