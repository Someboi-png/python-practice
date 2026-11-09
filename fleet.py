class Ship:
    def __init__(self, name, speed, fuel_per_hour):
        self.name = name
        self.speed = speed
        self.fuel_per_hour = fuel_per_hour

    def trip_fuel(self,distance):
        time = distance/self.speed
        return time * self.fuel_per_hour

ship1 = Ship("Orion", 15, 2.0)
ship2 = Ship("Ozon", 25, 3.0)
ship3 = Ship("Atlant", 20, 2.5)

ships = [ship1,ship2,ship3]

for ship in ships:
    fuel = ship.trip_fuel(300)
    print(f"{ship.name}: {fuel} т")

best_ship = min(ships, key=lambda ship: ship.trip_fuel(300))

print(f"Меньше всего топлива: {best_ship.name}, {best_ship.trip_fuel(300)} т")