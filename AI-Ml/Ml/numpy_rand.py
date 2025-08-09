import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.rand(100)*10
# print(x)
y = 3 * x + np.random.randn(100) * 2

m, c = np.polyfit(x, y, 1)

print(np.polyfit(x, y, 1))
print(f"Slope(m): {m:.2f}")
print(f"Intercept(c) : {c:.2f}")

newx = 7
print(f"Predicted y for x ={newx}: \n{m*newx + c:.2f} ")
plt.scatter(x, y, color="blue", alpha=0.6, label = "DataPoints")
plt.plot(x, m*x+c, color="red", lw=2, label="Best fitted line")
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.legend()
plt.show()