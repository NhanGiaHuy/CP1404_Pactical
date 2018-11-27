import random

quick_pick = int(input("how many quick picks do you wish to generate?\n"))
for i in range(quick_pick):
    for j in range(5):
        print(random.randint(1, 45), end="\t")
    print("")