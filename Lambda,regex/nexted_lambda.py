"""
(a+b)*c expression lambda evaluate and return to another lambda
"""

# num1 = int(input("enter value: "))
# num2 = int(input("Enter value: "))
# num3 = int(input("Enter value: "))

# l2 = lambda c: lambda a, b:(a+b)*c
# l1 = l2(num3)

# value = l1(num1, num2)
# print(value)

print((lambda a: lambda b,c:(a+b)*c)(5)(3,2))