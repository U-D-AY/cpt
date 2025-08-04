import pandas as pd

names = input("Enter 3 names seperated with spaces: ").strip().split()

indicies = input("enter 3 indicies labels: ").strip().split()

try:
    if len(names) != 3 or len(indicies) != 3:
        raise ValueError("Please provide 3 names and 3 indicies")
    series = pd.Series(data = names, index = indicies, name = "names")
    print(series)
except ValueError as e:
    print(f"Error as {e}")
