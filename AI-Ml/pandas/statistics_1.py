"""

Code to show thw computation of statitics and access
series attributes

print original data, which is serialized
statistics:
mean 
sum
max
min 
attribuites
index =['a', 'b',......]'
values = [100.0, ................]

"""

import pandas as pd

numbers = list(map(float, input("Enter 5 random number, space seprated: ").strip().split()))

try:
    if len(numbers) != 5:
        raise ValueError("Please provide 5 numbers.")
    series  = pd.Series(numbers, index = ['a', 'b', 'c', 'd', 'e'])
    print("\n Original series series: ")
    print(series)
    
    # Satistics
    print("\nStatistics: ")
    print(f"Count: {series.count()}\n")
    print(f"Mean: {series.mean()}\n")
    print(f"Median : {series.median()}\n")
    print(f"mode : \n{series.mode()}\n")
    print(f"Max: {series.max()}\n")
    print(f"Min: {series.min()}\n")
    print(f"Std: {series.std()}\n")
    print(f"Var: {series.var()}\n")
    print(f"Sum : {series.sum()}\n")
    
except ValueError as e:
    print(f"Error: {e}")