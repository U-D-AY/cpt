import pandas as pd

try:
    df = pd.read_csv("hospital_data.csv")
    series = df['Admission_Date']
    print("|nOriginal Admission_Date series: ")
    print(series)

    # convert string to datetime
    date_series = pd.to_datetime(series, format='%Y-%m-%d')
    print("\nAdmission Date series after converting to datetime: ")
    print(date_series)

    # Update and save the dataframe
    df['Admission_Date'] = date_series.dt.strftime('%d/%m/%Y')
    df.to_csv("hospital_data.csv", index= False)
    print("\nUpdate csv saved to 'hospital_data.csv'.")
    
except FileExistsError as e:
    print(f"Error: {e}")