import pickle


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hi(self):
        return f"Hello, my name is {self.name}."

s = Student('Uday', 66)

with open('student.pkl', 'wb') as file:
    pickle.dump(s, file)

with open('student.pkl', 'rb') as file:
    load_data = pickle.load(file)

print(load_data.name)
print(load_data.age)
print(load_data.hi())