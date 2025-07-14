st = input('enter string: ')

vowels = "aeiouAEIOU" 

sol = ""
a = 0 
for i in st:
    if i in vowels:
        sol+='z'
        a+=1
    else:
        sol+=i

print(sol,'no vowles' if not a else '')