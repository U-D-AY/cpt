import requests

url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    'tilte':'Kingdom',
    'body':'wipro geeks',
    'userId':101
    }
response = requests.post(url, json=data)

if response.status_code == 201:
    print('sucessful')
    print(F"Response : {response.json()}")