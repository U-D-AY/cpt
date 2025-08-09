import pickle

my_list = [26, 11, 24, 'uday', True]

with open('list.pkl', 'wb') as file:
    pickle.dump(my_list, file)

with open('list.pkl', 'rb') as file:
    loaded_list = pickle.load(file)

print(loaded_list)