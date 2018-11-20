def main():
    list_price = []
    total = 0
    number_item = int(input("Enter Number of Item: "))
    while number_item <= 0:
        print("invalid Number!")
        number_item = int(input("Enter Number of Item: "))
    for i in range(number_item):
        price = float(input("Price of Item: "))
        list_price.append(price)
        total = total + list_price[i]
    if total > 100:
        total = total - total*0.1
    print("Total price for " + str(number_item) + "item is $" + str(total))

main()