import numpy as np 

a = np.fromiter(map(int, input("Enter the value array: ").split()), dtype = float)
reshaped = a.reshape((3,3))

print("Reshaped :\n", reshaped)

linear = reshaped.reshape(-1)
print("Linear :\n",linear)