import pickle

with open("test1.pkl", "rb") as f:
    my_list = pickle.load(f)

print(my_list)
