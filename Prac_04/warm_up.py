NUMBER = [3, 1, 4, 1, 5, 0, 2]

def main():
    length = len(NUMBER)
    change_first_element()
    change_last_element(length)
    get_element()
    check_value()

def change_first_element():
    NUMBER[0] = 10
    print(NUMBER)

def change_last_element(length):
    NUMBER[length - 1] = 1
    print(NUMBER)

def get_element():
    new_number = NUMBER[1:-1]
    print(new_number)

def check_value():
    if 9 in NUMBER:
        print("9 is in the list")
    else:
        print("9 is not in the list")
main()