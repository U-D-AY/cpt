'''
Program to create a txt ,file acesses the file data and use the data to split the lines into series of words and ud=se space to perform 
split operation.
sample.txt
hello students
how are you today
'''

with open('sample.txt','w') as file:
    file.write('Hello students\n')
    file.write('How are you today\n')
    file.close()

with open('sample.txt','r') as file:
    a = [j for line in file.readlines() for j in line.strip().split()]
    print(a)