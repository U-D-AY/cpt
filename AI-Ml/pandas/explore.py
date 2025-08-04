import pandas as pd

try:
    df = pd.read_csv('hospital_data.csv')
    print('\nhospital dataframe: ')
    print(df)
    
    # display basic info
    print(f"\nDataFrame Info:")
    df.info()
    # Statistical info
    print(f"\nStatistical info: \n{df.describe()}")
    
except FileNotFoundError as e:
    print(f"Error: {e}")