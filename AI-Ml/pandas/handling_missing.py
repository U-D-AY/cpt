import pandas as pd 
import numpy as np

series  = pd.Series([10, np.nan, 30, np.nan, 60, np.nan, 80], index = ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(f"original series : \n{series}\n")

# Checking missing values
print(f"Missing Values: \n{pd.DataFrame({
    "values" : series,
    "isNaN" : series.isna()
    })}\nCount: ({series.isna().sum()})\n")

# if we want to replace 'nan' with '0'
filled_series = series.fillna(0)
print(f"The series after filling NaN's with 0:\n{filled_series}\n")

# froward fill
print(f"The series after filling NaN's with froward fill:\n{series.ffill()}\n")

# Backward fill
print(f"The series after filling NaN's with backward fill:\n{series.bfill()}\n")

# if we want delete the NaN's then
deleted_series = series.dropna()
print(f"The series after droping missing values:\n{deleted_series}\n")
