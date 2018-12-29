from Prac_08.taxi import Taxi

taxi_1 = Taxi("Prius 1", 100)
print(taxi_1.price_per_km)
print(taxi_1)

taxi_1.drive(40)

print(taxi_1)

taxi_1.start_fare()
print(taxi_1)

