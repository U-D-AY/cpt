import csv

with open('people.csv','w',newline="") as file:
    writer = csv.writer(file)
    writer.writerow(['namme', 'age'])
    for _ in range(2):
        name = input('Enter the Name: ')
        age = int(input('Enter age: '))
        writer.writerow([name,age])
    print('Data written on csv file')
