# json module

import json

name = input("Enter the name: ")
age = int(input('Enter age: '))

data = {'name':name, 'age':age}

stringify_json = json.dumps(data)
print(f"Stringified data : {stringify_json}, its type: {type(stringify_json)}")
