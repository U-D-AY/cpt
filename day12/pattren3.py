# a = int(input("enter:"))
# for i in range(1,a+1):
#     print(f"{" "*(a-i)}{int('1'*i)**2}")

a = int(input("enter:"))
for i in range(1,a+1):
    print(f" "*(a-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for k in range(j-1,0,-1):
        print(k,end="")
    print()