import pandas as pd

try:
    df = pd.read_csv('Hosipital_data_updated0.csv')
    print("\nOriginal Hosipital DataFrame")
    print(df)
    
    # groping by department
    g =df.groupby('Department')
    print(f"\nGroup by\n{g.groups}\n")
    
    bg = df.groupby('Department')['Bill']
    print(f"Group by with bill\n{bg.sum()}\n")
    
    grouped = df.groupby('Department')['Bill'].mean()
    print("\nAverage medical cost by Department")
    print(grouped)
    
except FileExistsError as e:
    print(f"Error: {e}")
    
    