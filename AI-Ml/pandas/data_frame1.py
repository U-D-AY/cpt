import pandas as pd 

data = {
    'Name' : ['Luffy', 'Asta', 'Itachi' ],
    'Age' : [20, 18, 26],
    'Branch' : ['CSE', "CSD", "MECH"]
}


dframe = pd.DataFrame({
**data
})

print(dframe)
print(dframe['Name'])
print(f"\nNames and branch cols: \n{dframe[['Name', 'Branch']]}")
print(f"\nRow 2: \n{dframe.iloc[2]}")

Stipend = [15000, 14000, 10000]
dframe.insert(1, 'Salary', Stipend)

print(f"\nUpdated Df: \n{dframe}")

dframe.at[2, 'Age'] = 22
print(f"\nAfter age Updaion: \n{dframe}")
