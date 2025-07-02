import json

name = input("Enter the name: ")
age = int(input('Enter age: '))

user = [{'name': name+f"{i}" if i!=0 else name,
         'age':age+i} 
         for i in range(10)
         ]

with open('user.json','w') as f:
    json.dump(user, f)

print('Data written to json folder')

with open('user.json','r') as f:
    loaded = json.load(f)
    print(f"read from files: {loaded}, type: {type(loaded)}")