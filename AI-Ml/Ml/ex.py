import matplotlib.pyplot as plt
import pickle

with open("plot.pkl", 'rb') as f:
    loadfig = pickle.load(f)

plt.show()