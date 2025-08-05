import pandas as pd

try:
    df = pd.read_csv("hospital_data.csv")
    series = df["Name"]
    print("\nOriginal names series: ")
    print(series)
    
    clean_series = series.str.title().str.strip()
    print("Name series after standardizing with (title case, stripped space): ")
    print(clean_series)
    
    # saving to csv file
    df['Name']= clean_series
    df.to_csv("hospital_data.csv")
    print("successfully saved.")
except FileNotFoundError as e:
    print(f"Error: {e}")