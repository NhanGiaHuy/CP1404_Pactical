INCOME = []
def main():
    number_month = int(input("how many month?"))
    insert_income(number_month)
    show_income_report()

def insert_income(number_month):
    for month in range(number_month):
        monthly_income = float(input("enter income for month " + str(month + 1)))
        INCOME.append(monthly_income)

def show_income_report():
    total = 0
    for month in range(len(INCOME)):
        total = total + INCOME[month]
        print("Month {} - Income: ${:10} Total: ${:10}".format(month + 1, INCOME[month], total))

main()