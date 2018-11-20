import random
def main():
    POPULATION = 1000
    MAX_INCREASE_BORN = 20
    MIN_INCREASE_BORN = 10
    MAX_DECREASE_DIED = 25
    MIM_DECREASE_DIED = 5
    print("Welcome to the Gopher Population Simulator\nStarting population: 1000")
    for year in range(1, 10):
        print("year {}\n*****".format(year))
        number_gopher_born = random_born(POPULATION, MAX_INCREASE_BORN, MIN_INCREASE_BORN)
        number_gopher_died = random_died(POPULATION, MAX_DECREASE_DIED, MIM_DECREASE_DIED)
        POPULATION = POPULATION + number_gopher_born - number_gopher_died
        print("{} gophers were born. {} died.\nPopulation: {}".format(number_gopher_born,number_gopher_died,POPULATION))

def random_born(population, max, min):
    number_gopher_born = round(population * (round(random.randint(min, max), 0)/100))
    return number_gopher_born

def random_died(population, max, min):
    number_gopher_died = round(population * (round(random.randint(min, max), 0)/100))
    return number_gopher_died

main()