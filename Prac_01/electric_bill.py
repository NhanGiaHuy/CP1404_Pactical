def Estimator_1():
    print("Electric bill estimator")
    price = int(input("Enter the cents per kWh: "))
    amount_enegy = float(input("Enter the daily use in kWh: "))
    billing_day = int(input("Enter number of billing days: "))
    total_bill = (amount_enegy * billing_day * price) / 100
    print("Estimated bill: $" + str(total_bill))

def Estimator_2():
    print("Electric bill estimator 2.0")
    type_tariff = int(input("which tariff? 11 or 13: "))
    while  type_tariff != 13 and type_tariff != 11:
        print("invalid type! Please enter again!")
        type_tariff = int(input("which tariff? 11 or 13: "))
    if type_tariff == 11:
        price_tariff = 0.244618
    else:
        price_tariff = 0.136928
    amount_enegy = float(input("Enter the daily use in kWh: "))
    billing_day = int(input("Enter number of billing days: "))
    total_bill = (amount_enegy * billing_day * price_tariff)
    print ("Estimated bill : $" + str(round(total_bill, 2)))

Estimator_2()