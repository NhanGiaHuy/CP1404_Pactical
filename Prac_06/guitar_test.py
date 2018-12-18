from Prac_06.guitar import Guitar


my_guitar = []
str1 = ""
name = str(input("Name: "))
year = int(input("Year: "))
cost = float(input("Cost: "))

while name != "":
    print("{} ({}) : ${:,} added.".format(name, year, cost))
    str1 = str1 + name + "," + str(year) + "," + str(cost)
    my_guitar.append(str1)
    name = str(input("Name: "))
    if name == "":
        break;
    year = int(input("Year: "))
    cost = float(input("Cost: "))

for i in range(len(my_guitar)):
    guitar = my_guitar[i].split(",")
    guitar = Guitar(guitar[0], int(guitar[1]), guitar[2])
    print("Guitar {}: {:>10} ({}), worth ${:>15}".format(i+1, guitar.get_name(), guitar.get_year(), guitar.get_cost()), end="")
    guitar.get_age()
    if guitar.is_vintage() == True:
        print("(Vintage)", end="\n")
    else:
        print("", end="\n")




