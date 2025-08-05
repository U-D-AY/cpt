import pandas as pd

try:
    df = pd.read_csv("hospital_data.csv")
    series = df["Bill"]
    print('\n Original Hospital Bill: ')
    print(series)

    # User manual Input
    patient_id = input("\nEnter Patient_ID to update: \n").strip()
    assert patient_id in df['Patient_Id'].values, f"Invalid Patient ID: '{patient_id}'"
    
    new_cost = float(input("\nEnter new Bill for Patient: {patient_id}:").strip())
    assert new_cost >=0, "Amount:{new_cost} can't be Negative."
    
    # Update bill series and save
    index = df[df['Patient_Id'] == patient_id].index[0]
    series[index] = new_cost
        
    print("\nUpdated Medical series:")
    print(series)
    
    # Update DataFrame and Save
    df['Bill'] = series
    df.to_csv('hospital_data.csv',index = False)
    print("Updated csv saved to hospital")
        
    
    
    
except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")