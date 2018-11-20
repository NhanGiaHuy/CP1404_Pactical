def main():
    x = int(input("Enter x"))
    y = int(input("Enter y"))
    user_choice = str(input("1. Show the even numbers from x to y\n2. Show the odd numbers from x to y\n3. Show the squares from x to y\n4. Exit the program\n"))
    while user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4":
        print("invalid value")
        user_choice = str(input("1. Show the even numbers from x to y\n2. Show the odd numbers from x to y\n3. Show the squares from x to y\n4. Exit the program\n"))
    while user_choice != "4":
        if user_choice == "1":
            if x > y:
                for i in range(x, y, -1):
                    if i % 2 == 0:
                        print(i, end=' ')
                print()
            else:
                for i in range(x, y, 1):
                    if i % 2 == 0:
                        print(i, end=' ')
                print()
        elif user_choice == "2":
            if x > y:
                for i in range(x, y, -1):
                    if i % 2 != 0:
                        print(i, end=' ')
                print()
            else:
                for i in range(x, y, 1):
                    if i % 2 != 0:
                        print(i, end=' ')
                print()
        elif user_choice == "3":
            if x > y:
                for i in range(x, y, -1):
                    print(pow(i, 2), end=' ')
                print()
            else:
                for i in range(x, y, 1):
                    print(pow(i, 2), end=' ')
                print()
        user_choice = str(input("1. Show the even numbers from x to y\n2. Show the odd numbers from x to y\n3. Show the squares from x to y\n4. Exit the program\n"))
    print("Finished")

main()