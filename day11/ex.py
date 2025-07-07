with open('file1.txt','r') as file:
    seperate_lines = [line.strip() for line in file.readlines()]
    print(seperate_lines)

file.close()
