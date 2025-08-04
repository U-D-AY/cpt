import pandas as pd

numbers  = list(map(int, input("Enter 4 numbers :").strip().split()))

try:
    if len(numbers) != 4:
        raise ValueError("Give 4 number only!")
    
    series = pd.Series(numbers, index=['a', 'b', 'c', 'd'])
    print('\nOrginal series:')
    print(series)
    
    # Doubling vectors
    double = series*2
    print(f"\nSeries after doubling it: \n{double}\n")
    
    # add 100
    add = series+100
    print(f"Series after adding 100: \n{add}\n")
    
    
except ValueError as e:
    print(f"Error: {e}")