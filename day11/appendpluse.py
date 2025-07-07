with open('file1.txt','a+') as file:
    file.write('\nappended data.')
    file.seek(0)
    print(file.read())