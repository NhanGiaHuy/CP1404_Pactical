"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""

    def __init__(self, name, fuel):
        """Initialise a Car instance.
        fuel: float, one unit of fuel drives one kilometre
        """
        self.fuel = fuel
        self.odometer = 0
        self.name = name

    def __str__(self):
        return "name: {}, fuel: {}, odo: {}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount
        print("add {} units of fuel".format(amount))

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
            print("The car drove {} km and ran out of fuel".format(distance))
        else:
            self.fuel -= distance
            print("The car drove {}".format(distance))
        self.odometer += distance
        return distance