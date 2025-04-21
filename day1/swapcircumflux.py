"""
a,b=b,a

a = a+b
b = a-b
a = a-b

a = a*b
b = a//b
a = a//b
"""

'''for i in range(5):
    a = int(input())
    b = int(input())
    a = a^b
    b = a^b
    a = a^b
    print(f"a:{a}\nb:{b}")'''


'''for i in range(5):
    a = int(input())
    b = int(input())
    t = a
    a = (a|b)&b
    b = (temp|b)&b
    print(f"a:{a}\nb:{b}")'''

'''for i in range(5):
    d={}
    d['a'] = int(input())
    d['b'] = int(input())
    
    d['a'] = d['b']
    d['b'] = d['a']
    print(f"a:{d['a']}\nb:{d['b'}") '''

''' import itertools

gen = iter([1,2,3])
lst = list(gen) '''


print([x**2 for x in range(1,10+1)if x%2==0])

print([x**2 if x%2==0 else x**3 for x in range(1,10+1)])
