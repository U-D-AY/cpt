import pandas as pd
 
try: 
    df = pd.read_csv('Hosipital_data.csv')
    print("\nOriginal values: ")
    print(df)
    
    # check missing values
    print("\nMissing Values")
    print(df.isna())
    
    # Filling names by unknown 
    df_filled = df.copy()
    df_filled["Name"] = df_filled['Name'].fillna('Unknown')
    df_filled['Age'] = df_filled['Age'].fillna(df_filled['Age'].mean())
    df_filled['Bill'] = df_filled['Bill'].fillna(0)
    df_filled['Department'] = df_filled['Department'].ffill()
    df_filled['Admission_Date'] = df_filled['Admission_Date'].ffill()
    
    print("\nDataframe after filling by default: \n")
    print(df_filled,"\n")
    
    df_filled.to_csv("Hosipital_data_updated0.csv", index=False)
    print("The file have updated.")
    
except FileNotFoundError as e:
    print(f"Error: {e}")