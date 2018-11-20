def main():
    MAX_NUMBER = 127
    MIN_NUMBER = 33
    choice = int(input("main menu\n1.character --> ASCII code\n2.ASCII code -->character\n3.ascii table\n4.quit\n"))
    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print("invalid choice!")
        choice = int(input("main menu\n1.character --> ASCII code\n2.ASCII code -->character\n3.ascii table\n4.quit\n"))
    while choice != 4:
        if choice == 1:
            character = str(input("enter character\n"))
            while len(character) > 1:
                character = str(input("please enter single character\n"))
            ascii_code = ord(character)
            print("The ASCII code for {} is {}".format(character, ascii_code))
        elif choice == 2:
            number = get_number(MIN_NUMBER,MAX_NUMBER)
            character = chr(number)
            print("The character for {} is {}".format(number, character))
        else:
            number_column = int(input("how many column do you want to print in ascii table?\n"))
            number_row = (MAX_NUMBER + MIN_NUMBER + 1) // number_column
            for row in range(number_row + 1):
                starting_value = MIN_NUMBER + row
                value = starting_value
                for column in range(number_column - 1):
                    print_value = value + (number_row * column)
                    print("{:6} {:>2}".format(print_value, chr(print_value)), end="")
                    value += 1
            value_to_print = value + ((column + 1) * number_row)
            if value_to_print <= MAX_NUMBER:
                print("{:6} {:>2}".format(value_to_print, chr(value_to_print)), end="")
            print()
        choice = int(input("\nmain menu\n1.character --> ASCII code\n2.ASCII code -->character\n3.ascii table\n4.quit\n"))
    print("thank you for using program!")


def get_number(lower, upper):
    while True:
        try:
            number = int(input("enter number between {} and {}\n".format(lower, upper)))
            if number >= 33 and number <= 127:
                break
            else:
                print("invalid number\n")
        except ValueError:
            print("invalid number\n")
    return number




main()
