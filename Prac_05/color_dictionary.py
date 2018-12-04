
COLOR_LIST = {"AliceBlue": "#f0f8ff", "aquamarine1": "#7fffd4", "azure1": "#f0ffff", "blue1": "#0000ff", "BlueViolet": "#8a2be2"}

color = input("Enter name of color ")
while color != "":
    if color in COLOR_LIST:
        print(color, "is", COLOR_LIST[color])
    else:
        print("Invalid short state")
    color = input("Enter short state: ")