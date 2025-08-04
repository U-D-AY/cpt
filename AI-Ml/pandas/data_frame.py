import pandas as pd 

# data = {
#     'Name' : ['Luffy', 'Asta', 'Itachi' ],
#     'Age' : [20, 18, 26],
#     'Branch' : ['CSE', "CSD", "MECH"]
# }


n = int(input("Enter number of records: "))
names = []
ages = []
branches = []

for i in range(n):
    print(f"------------enter:{i+1}--------------")
    
    name = input('Enter names: ').strip()
    age = int(input("Enter Age: ").strip())
    branch = input("Enter the Branch: ").strip()
    
    names.append(name)
    ages.append(age)
    branches.append(branch)

dframe = pd.DataFrame({
    'Names':names,
    'Age' : ages,
    "Branchs": branches
})
print(dframe)