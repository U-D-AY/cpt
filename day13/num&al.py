a = int(input("enter: "))
for i in range(1,a+1):
    s = " "*(a-i)
    n = ''.join([f"{j}" for j in range(1,i+1)])
    alp = ''.join([chr(j) for j in range(65+i-2,64,-1)])
    print(s+n+alp)

    