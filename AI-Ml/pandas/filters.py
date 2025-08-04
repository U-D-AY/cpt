import pandas as pd

numbers = list(map(float, input("Enter 4 random values separated by commas: ").strip().split()))

try :
    if len(numbers) != 4:
        raise ValueError("Please provide exactly 4 numbers: ")
    total_data = pd.Series(numbers)
    print(total_data)

    filtered = total_data[total_data>10]

    print("values > 10: ")
    print(filtered)

except ValueError as e:
    print(f"Error :{e}")


