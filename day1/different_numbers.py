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

    
    
