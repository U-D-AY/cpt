"""
Code elaborates how to filter string data in series based on insensitivity 
"""

import pandas as pd

strings = input("enter 5 strings, space separated: ").strip().split()

substring = input('enter substring: ').strip()

try: 
    if len(strings) != 5:
        raise ValueError("Please provide 5 strings only.")
    
    str_series = pd.Series(strings)
    print("Original Series: ")
    print(str_series)
    
    filtered_series = str_series[str_series.str.lower().str.contains(substring.lower(),na=False)]
    
    print(f"Strings containing '{substring}'(case-insensitive),")
    print(filtered_series if not filtered_series.empty else "No Match Found.")
    
except ValueError as e:
    print(f"Error: {e}")