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

    
    
