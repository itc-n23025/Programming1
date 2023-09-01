import my_math


def my_pow(x, y):
    return x**y


with open("my_math.py", "w") as f:
    f.write(
        """def my_pow(x,y):
    return x ** y\n"""
    )
my_math.my_pow(2, 5)
