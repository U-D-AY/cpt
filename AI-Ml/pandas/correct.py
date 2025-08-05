import numpy as np
import pandas as pd

try:
    df = pd.read_csv("hospital_data.csv")
    series = df['Age']
    print("Original Series: ")
    print(series)
    
    # replace invalid ages, <0 and >120 with NaN
    clean_series = series.where((series>=0)&(series<=120), np.nan)
    print("\nAge series after replacing invalid ages with NaN: ")
    print(clean_series)
    
except FileExistsError as e:
    print(f"Error: {e}")