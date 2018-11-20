
def main():
    celsius_temperature = float(input("Enter the temperature in Celsius format"))
    fahrenheit_temperature = Celsius_to_Fahrenheit(celsius_temperature)
    print(fahrenheit_temperature)
    fahrenheit_temperature = float(input("Enter the temperature in Fahrenheit format"))
    celsius_temperature = Fahrenheit_to_Celsius(fahrenheit_temperature)
    print(str(round(celsius_temperature, 2)))


def Celsius_to_Fahrenheit(celsius_temperature):
    fahrenheit_temperature = (celsius_temperature * (9/5)) + 32
    return fahrenheit_temperature

def Fahrenheit_to_Celsius(fahrenheit_temperature):
    celsius_temperature = (fahrenheit_temperature - 32) * (5/9)
    return celsius_temperature

main()