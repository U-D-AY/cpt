import pandas as pd
import numpy as np

data = {
    'Patient_Id' : ['P001', 'P002', "P003", 'P004', 'P005', 'P006'],
    'Name' : ['Luffy', 'Jin', 'leon', 'Itachi', 'Ichigo', None],
    'Age' : [22, 26, 29, None, 25, 18],
    'Department' : ['Cancer', "Neurology", 'Cardiology', None, 'Cancer', None],
    'Admission_Date' : ['2025-01-5', None, '2025-02-12', '2025-05-6', '2025-06-16', '2025-07-31'],
    'Bill' : [100000, 200000, 300000, None, 400000, 600000]
}

df = pd.DataFrame(data)
df.to_csv('hospital_data.csv', index=False)
print("Sucessfully created csv file.")