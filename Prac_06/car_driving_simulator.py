from Prac_06.car import Car
def main():
    print("Let's drive!")
    car_name = str(input("Enter your car name"))
    my_car = Car(car_name)
    print("{}, fuel = {}, odo = {}".format(my_car.name, my_car.fuel, my_car.odometer))
    menu_choice = insert_menu()
    while menu_choice.lower() == "d" or menu_choice.lower() == "r":

        if menu_choice.lower() == "d":
            while True:
                try:
                    distance = float(input("how many km you want to drive? "))
                    while distance < 0:
                        print("the distance must be >=0")
                        distance = float(input("how many km you want to drive? "))

                    break;
                except ValueError:
                    print("Invalid Input Value")
            my_car.drive(distance)
            print("{}, fuel = {}, odo = {}".format(my_car.name, my_car.fuel, my_car.odometer))
            menu_choice = insert_menu()
        else:
            while True:
                try:
                    amount = float(input("How many units of fuel do you want to add to the car? "))
                    while amount < 0:
                        print("Fuel amount must be >= 0")
                        amount = float(input("How many units of fuel do you want to add to the car? "))

                    break;
                except ValueError:
                    print("Invalid Input Value")
            my_car.add_fuel(amount)
            print("{}, fuel = {}, odo = {}".format(my_car.name, my_car.fuel, my_car.odometer))
            menu_choice = insert_menu()


def insert_menu():
    while True:
        try:
            menu_choice = str(input("Menu\nd) drive\nr) refuel\nq) quit\nEnter your choice: "))
            while menu_choice.lower() != "d" and menu_choice.lower() != "r" and menu_choice.lower() != "q":
                print("Invalid input value!")
                menu_choice = str(input("Menu\nd) drive\nr) refuel\nq) quit\nEnter your choice: "))
            break;
        except ValueError:
            print("Invalid input value!")
    return menu_choice


main()