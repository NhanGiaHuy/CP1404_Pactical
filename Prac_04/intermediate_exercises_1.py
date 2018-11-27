NUMBER = []

def main():
    for position in range(5):
        number = int(input("Enter Number"))
        NUMBER.append(number)

    print("the first number is: " + str(NUMBER[0]))
    print("the last number is: " + str(NUMBER[-1]))
    min_number = find_min()
    print("the smallest number is:" +  str(min_number))
    max_number = find_max()
    print("the largest number is:" + str(max_number))
    average = find_average()
    print("the average of the number is:" + str(average))
def find_min():
    min_value = NUMBER[0]
    for value in NUMBER:
        if value < min_value:
            min_value = value
    return min_value



def find_max():
    max_value = NUMBER[0]
    for value in NUMBER:
        if value > max_value:
            max_value = value
    return max_value

def find_average():
    total = 0
    for value in NUMBER:
        total += value
    average = total / len(NUMBER)
    return  average


main()