from car import Car

def main():
    bus = Car(180, 'Bus')
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    limo = Car(100, 'Limo')
    limo.add_fuel(20)
    print("fuel =", limo.fuel)

    limo.drive(115)
    # print("fuel= ", limo.fuel)
    print("odo =", limo.odometer)
    print(limo)
main()