print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12")
first = input("Select first service: \n")
second = input("Select second service: \n")
num1 = 0
num2 = 0
total = num1 + num2
serv_oil = 35
serv_wax = 12
serv_tire = 19
serv_wash = 7
print("Davy's auto shop invoice\n")
if first == "Oil change":
    print("Service 1: Oil change, $35")
    num1 = 35
elif first == "Car wax":
    print("Service 1: Car wax, $12")
    num1 = 12
elif first == "Tire rotation":
    print("Service 1: Tire rotation, $19")
    num1 = 19
elif first == "Car wash":
    print("Service 1: Car wash, $7")
    num1 = 7
elif first == "-":
    print("Service 1: No service")
if second == "Oil change":
    print("Service 2: Oil change, $35\n")
    num2 = 35
elif second == "Car wax":
    print("Service 2: Car wax, $12\n")
    num2 = 12
elif second == "Tire rotation":
    print("Service 2: Tire rotation, $19\n")
    num2 = 19
elif second == "Car wash":
    print("Service 2: Car wash, $7\n")
    num2 = 7
elif second == "-":
    print("Service 2: No service\n")
print("Total: $", total)
