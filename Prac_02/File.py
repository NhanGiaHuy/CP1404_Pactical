def one():
    user_name = str(input("enter your name: "))
    out_file = open("name.txt", "w")
    print(user_name, file = out_file)
    out_file.close()

def two():
    out_file = open("name.txt", "r")
    print("your name is " + out_file.read())
    out_file.close()

def three():
    file = open("number", "r")
    a = int(file.readline())
    b = int(file.readline())
    print(a + b)
    file.close()

def four():
    total = 0.0
    file = open("numbers", "r")
    for i in file:
        total += float(i)
    print("the total is:{:.2f}".format(total))
    file.close()

four()