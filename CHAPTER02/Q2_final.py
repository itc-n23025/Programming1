import random

while True:
    random_list = chr(random.randint(97, 122))
    print(random_list)

    if random_list == "h":
        break
