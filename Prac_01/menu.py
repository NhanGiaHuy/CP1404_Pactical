def main():
    user_name = str(input("Enter Name: "))
    print("(H)ello\n(G)oodbye\n(Q)uit\n")
    user_choice = str(input("Please Enter Choice!\n"))
    while user_choice.upper() != "H" and user_choice.upper() != "G" and user_choice != "Q":
        print("invalid menu!")
        user_choice = str(input("Please Enter Choice!\n"))
    while user_choice.upper() != "Q":
        if user_choice.upper() == "H":
            print("Hello " + user_name)
        else:
            print("Goodbye " + user_name)
        user_choice = str(input("Please Enter Choice!\n"))
    print("Finished")

main()