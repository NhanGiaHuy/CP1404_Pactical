from datetime import datetime
now = datetime.now()

NAME = []
DOBS = []
LIST_NAME = {}

for i in range(5):
    name = str(input("Name: "))
    LIST_NAME[name] = str(input("Day of Birth: "))

for key in LIST_NAME:
    date_of_birth = LIST_NAME[key].split("/")
    age = now.year - int(date_of_birth[-1])
    print("Name: {:<10} Date of Birth{:<10} Age{:<5}".format(key, LIST_NAME[key], age))



