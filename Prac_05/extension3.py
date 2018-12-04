
TARIFF = {"11": 0.244618, "31": 0.136928, "22": 0.152412}
print("Electricity Bill Estimator 2.0")
type_tariff = str(input("Which tariff? 11 or 31: "))

while type_tariff != "13" and type_tariff != "11" and type_tariff != "22":
    print("invalid type! Please enter again!")
    type_tariff = int(input("which tariff? 11 or 13 or 22: "))
price_tariff = TARIFF[type_tariff]

daily_use = float(input("Enter daily use in kWh: "))

billing_days = int(input("Enter number of billing days: "))

total_bill = (daily_use * billing_days * price_tariff)

print ("Estimated bill : $" + str(round(total_bill, 2)))