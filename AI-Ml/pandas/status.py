import pandas as pd

try:
    df = pd.read_csv('Hosipital_data_updated0.csv')
    print("\nOriginal Hosipital DataFrame")
    print(df)
    
    # Add a status column, based on age
    df['Status'] = df['Age'].apply(lambda x: "Senior" if x>=50 else "Adult" if x>=18 else "Unknown")
    print('\nDataframe with Status column:')
    print(df)
    
    # saving to csv
    df.to_csv("Hosipital_data_updated1.csv", index=False)
    print(f"Modified Datarame saved to 'Hosipital_data_updated1.csv'.")
    
    
except FileExistsError as e:
    print(f"Error: {e}")