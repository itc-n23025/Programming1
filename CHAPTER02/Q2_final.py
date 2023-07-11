# rint([chr(ord("a") + i) for i in range(26)])
# rint()
import random

while True:
    random_letter = chr(random.randint(97, 122))  # ランダムなアルファベットを生成する
    print(random_letter)

    if random_letter == "h":
        break
