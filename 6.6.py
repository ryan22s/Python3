goes_in = input("Please enter a string: \n")
while goes_in != 'q':
    while goes_in.count(',') == 0:
        print("Error: No comma in string.")
        goes_in = input("Please enter a string: \n")
    entered = goes_in.split(',')
    print(f"First word: {entered[0].strip()}\nSecond word: {entered[1].strip()}\n\n")
    goes_in = input("Please enter a string: \n")
