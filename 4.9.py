cost_oil_change = '$35'
cost_tire_rotation = '$19'
cost_car_wash = '$7'

oil_change = input("Enter desired auto service: ")
print("You entered: %s" % oil_change)
if oil_change == 'Oil change':
    print(f"Cost of oil change: {cost_oil_change}\n")
elif oil_change == "Car wash":
    print(f"Cost of car wash: {cost_car_wash}\n")
elif oil_change == "Tire rotation":
    print(f"Cost of tire rotation: {cost_tire_rotation}")
else:
    print("Requested service is not recognized.")
