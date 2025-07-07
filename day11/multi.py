with open('file1.txt','r') as file,open('file2.txt','r')as file2:
    content1 = file.read()
    content2 = file2.read()
    print('Data of file1:',content1)
    print('Data of file2:',content2)
    file.close()
    file2.close()