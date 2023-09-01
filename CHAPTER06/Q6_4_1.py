import random

random.seed(1)
msgs = [
    "Hi",
    "Hello",
    "Good morning",
    "Good night",
    "See you later",
    "How are you",
    "Have good day",
]
with open("some.txt", "w") as f:
    for i in range(1000000):
        f.write("{},{}\n".format(i, random.choice(msgs)))

f = open("some.txt")
print(next(f), end="")
print(next(f), end="")
f.close()
