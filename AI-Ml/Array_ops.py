import numpy as np

a1 = np.array([2, 3, 4, 5, 6])
a2 = np.array([7, 8, 9, 1, 2])

print("Adddition :\n", a1+a2)
print("Product :\n", a1*a2)
print("Squre :\n", a1**2)
print("sin: \n", np.sin(a1))
print("cos: \n", np.cos(a1))
print("tan: \n", np.tan(a1))
print("cot: \n", 1/np.tan(a1))
print("mean: \n", np.mean(a1))
print("min: \n", np.min(a1))
print("max: \n", np.max(a1))
print("argmax: \n", np.argmax(a1))
print("Std: \n", np.std(a1))
print("log: \n", np.log(a1))

print()