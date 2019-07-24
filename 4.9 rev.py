# Set pricing for services offered
cost_oil_change = '$35'
cost_tire_rotation = '$19'
cost_car_wash = '$7'
# Ask the user for service desired
service = input("Enter desired auto service: ")
# Show the user their selection
print(f"You entered: {service}")
# Select the service desired and print its cost
if service == 'Oil change':
    print(f"Cost of oil change: {cost_oil_change}")
elif service == "Car wash":
    print(f"Cost of car wash: {cost_car_wash}")
elif service == "Tire rotation":
    print(f"Cost of tire rotation: {cost_tire_rotation}")
else:
    # If service is not defined, print error
    print("Requested service is not recognized.")
