def main():
    """
    Car shop style example. Prints the menu, then asks for input and puts in lower-case
    After that, it is matched or the else outputs the error message.
    :return nothing is returned:
    """

    cost = {
        'oil change': 35,
        'tire rotation': 19,
        'car wash': 7
    }
    menu = "Oil Change, Tire Rotation or Car Wash\n"
    menu_prompt = True
    while menu_prompt:
        print(menu)
        service = input("Enter desired auto service (q to quit): ").strip().lower()
        if service == 'q':
            print("Thank you.")
            # quit the program
            menu_prompt = False
        elif service in cost:
            # easiest solution to get it out of the dict.
            for key, value in cost.items():
                service_option = key
                service_cost = value
                if service == service_option:
                    print(f"You selected: {service_option}.\nCost of {service_option}: ${service_cost}\n")
        else:
            print("Requested service is not recognized.\n")


main()
