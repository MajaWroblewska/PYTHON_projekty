import random

with open('plik1.txt', 'w') as f:
    for i in range(93091):
        f.write(f"{random.randint(0,9)} {random.randint(0,9)} {random.randint(0,9)} {random.randint(0,9)} {random.randint(0,9)}\n")
