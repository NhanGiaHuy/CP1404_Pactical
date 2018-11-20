def main():
    sales = float(input("Enter sales: $ "))
    while sales >= 0:
        if sales >= 1000:
            user_bonus = 0.15 * sales
        else:
            user_bonus = 0.1 * sales
        print("user's bonus = " + str(user_bonus))
        sales = float(input("Enter sales: $ "))
main()