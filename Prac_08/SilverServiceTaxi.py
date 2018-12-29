from Prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.flag_fall = 4.50
        self.fanciness = fanciness
        self.current_fare_distance = 0
        self.price_per_km = self.price_per_km * self.fanciness

    def __str__(self):
        return "{} plus flagfall of ${}".format(super().__str__(), self.flag_fall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = self.flag_fall

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        return distance_driven
