import pandas as pd

try:
    df = pd.read_csv('hospital_data.csv')
    print("\nOriginal Hospital DataFrame")
    print(df)

    # Adding a discount column (10%)
    df['Discount'] = df['Bill']*0.9
    
    sorted_df = df.sort_values('Bill', ascending=False)
    print("\nSorted by Medical Bill(descending order)")
    print(sorted_df)
    
except FileExistsError as e:
    print(f"Error: {e}")