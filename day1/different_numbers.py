'''
#number manuplations in python
1.arm strong
2.strong number same as krishnamurthy's number
4.nivens number same as harsads
6.happy
7.atomorphic
8.adam's
9.magic
'''
'''
a = 145
t = a
s = 0
while a>0:
    d = a%10
    f = 1
    for i in range(1,d+1):
        f*=i
    s += f
    a//=10
if t == s:
    print('sucess')
else:
    print("fail")

'''

'''
a = 156
t = a
s = 0
while a>0:
    d = a%10
    s += d
    a//=10
if t%s == 0:
    print('nivens number')
else:
    print("not")
'''

'''
num = int(input("enter a number :"))
visit = set()
while num!=1 and num not in visit:
    visit.add(num)
    s = 0
    temp = num
    while temp>0:
        d = temp%10
        s+=d**2
        temp//=10
    num = s
if num == 1:
    print("happy")
else:
    print("not happy")

'''
