from Prac_08.car import Car
import random
class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability
        self.distance_driven = 0

    def __str__(self):
        return "{}, reliability: {}, distance: {}".format(super().__str__(), self.reliability, self.distance_driven)

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""

        rand = random.randint(0, 100)
        if rand < self.reliability:
            self.distance_driven = super().drive(distance)
            return self.distance_driven
        else:
            return self.distance_driven

