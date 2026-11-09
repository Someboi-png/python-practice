class Ship:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def trip_time(self, distance):
        return distance/self.speed

ships = Ship("Orion", 15), Ship("Ozon", 25), Ship("Atlant", 20)

while True:
    name = input("Какое судно? ")

    if name.lower() == "выход":
        print("До свидания")
        break

    found = False

    for ship in ships:
        if ship.name.lower() == name.lower():
            found = True

            while True:
                try:
                    distance = float(input("Расстояние в милях? "))
                    if distance <= 0:
                        print("Расстояние должно быть больше 0 ")
                        continue
                    break
                except ValueError:
                    print("Нужно ввести число")

            time = ship.trip_time(distance)

            print(f"{ship.name}: {time:.1f} ч до порта. ")
            break

    if not found:
        print("Такого судна нету в списке. ")
