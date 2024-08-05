import requests

data = {
    'id': 1,
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.put('https://reqres.in/api/users/2', json=data)
print(response.status_code)
print(response.json())
