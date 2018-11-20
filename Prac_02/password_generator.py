import random

MIN_LENGTH = 5
MAX_LENGTH = 15
CHARACTERS = "qwertyuiopasdfghjklzxcvbnm"
NUMERIC = "0123456789"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
password = ""
while True:
    try:
        password_length = int(input("enter length of password between {} and {}".format(MIN_LENGTH, MAX_LENGTH)))
        if password_length >= 5 and password_length <= 15:
            break
        else:
            print("invalid password length! Please enter again!")
    except ValueError:
        print("invalid password length! Please enter again!")
while True:
    try:
        number_upper_character = int(input("enter number of upper character"))
        if number_upper_character <= password_length:
            for i in range(0, number_upper_character):
                password += random.choice(CHARACTERS.upper())
            break
        else:
            print("total number of character must be less than or equal {}".format(password_length))
    except ValueError:
        print("total number of character must be less than or equal {}".format(password_length))

while True:
    try:
        number_special_character = int(input("enter number of special character"))
        if number_upper_character + number_special_character <= password_length:
            for i in range(0, number_special_character):
                password += random.choice(SPECIAL_CHARACTERS)
            break
        else:
            print("total number of character must be less than or equal {}".format(password_length))
    except ValueError:
        print("total number of character must be less than or equal {}".format(password_length))

while True:
    try:
        number_numeric = int(input("enter number of numeric"))
        if number_upper_character + number_special_character + number_numeric <= password_length:
            for i in range(0, number_numeric):
                password += random.choice(NUMERIC)
            break
        else:
            print("total number of character must be less than or equal {}".format(password_length))
    except ValueError:
        print("total number of character must be less than or equal {}".format(password_length))

for i in range(0, password_length - number_upper_character - number_numeric - number_special_character):
    password += random.choice(CHARACTERS)
print("your password is {}".format(password))