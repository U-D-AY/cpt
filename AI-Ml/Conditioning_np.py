import numpy as np 

a = np.fromiter(map(int, input("Enter the value array: ").split()), dtype = float).reshape((3,3))

print(f"The array: \n{a}")

# conditioning..

a = a.flatten()
print("Grater then 5: \n",a[a>5])
print("Less then 5: \n",a[a<5])




