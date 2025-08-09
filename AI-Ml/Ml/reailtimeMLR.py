import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([
        [3, 40, 1, 2.0],
        [2, 50, 2, 1.5],
        [4, 30, 3, 2.5],
        [1, 20, 4, 1.0],
        [2, 50, 2, 1.5],
        [4, 60, 1, 1.5],
        [7, 85, 3, 1.6],
        [6, 66, 2, 1.6]
    ])
y = np.array([20, 15, 25, 10, 12, 22, 18, 11])

model = LinearRegression()
model.fit(x, y)

print("Intercept: ", model.intercept_)
print("Coefficient: ", model.coef_)

newcar = np.array([[4, 55, 2, 1.8]])
pridict_price = model.predict(newcar)
print(f"Predicted price for the car: ${pridict_price[0]*1000:.2f}")

y_pred = model.predict(x)
plt.scatter(y, y_pred, color="orange")
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.xlabel("Actual Price")
plt.ylabel("Predicted prize in $1000")
plt.title("Original vs Pridicted")
plt.show()
