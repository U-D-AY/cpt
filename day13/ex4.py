# from collections import Counter

# a = input("enter string: ")

# print(Counter(a))

d = {}
for i in input("Enter : "):
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

print(d)