from Prac_08.taxi import Taxi
from Prac_08.SilverServiceTaxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
 SilverServiceTaxi("Hummer", 200, 4)]

def main():
    print("Let's drive!")
    menu_choice = insert_main_menu()
    bill_to_date = 0
    while menu_choice.lower() == "d" or menu_choice.lower() == "c":
        if menu_choice.lower() == "c":
            for i in range(len(taxis)):
                print("{} {}".format(i, taxis[i]))
            taxi_choice = insert_taxi_menu()
            print("Bill to Date: ${}".format(bill_to_date))
        else:
            if taxi_choice == None:
                print("Please choose taxi first!")
            else:
                distance = int(input("Drive how far? "))
                taxis[taxi_choice].drive(distance)
                bill_to_date += taxis[taxi_choice].price_per_km * distance
                print("Your {} trip cost you ${}".format(taxis[taxi_choice].name, bill_to_date))
                print("bill to date: ${}".format(bill_to_date))
        menu_choice = insert_main_menu()



def insert_main_menu():
    while True:
        try:
            menu_choice = str(input("q)uit\nc)hoose taxi\nd)rive"))
            while menu_choice.lower() != "q" and menu_choice.lower() != "c" and menu_choice.lower() != "d":
                print("Invalid input value!")
                menu_choice = str(input("q)uit\nc)hoose taxi\nd)rive"))
            break;
        except ValueError:
            print("Invalid input value!")
    return menu_choice

def insert_taxi_menu():
    while True:
        try:
            menu_choice = int(input("Choose Taxi: "))

            while menu_choice != 0 and menu_choice != 1 and menu_choice != 2:
                print("Invalid input value!")
                menu_choice = int(input("Choose Taxi: "))
            break;
        except ValueError:
            print("Invalid input value!")
    return menu_choice


main()