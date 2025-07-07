# with open('File1.txt','r') as file:
#     lines = file.readlines()

# print('List of lines: ',lines)

with open('File1.txt','r') as file:
     lines = file.readlines()

for line in lines:
     print(line.strip())