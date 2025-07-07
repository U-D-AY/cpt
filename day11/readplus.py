with open('file1.txt','r+') as file:
    content = file.read()
    file.seek(0)
    file.write('modification done.')