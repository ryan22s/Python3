dogs = [[0, 1, 3, 33], [31, 19, 90, 42]]

print(dogs)
print(dogs[0][3])
for i in dogs:
    print(i, end='...', flush=True)



# Let's play around with some lists and dicts

mod_choices = ('a', 'e', 'i', 'r', 'v', 's', 'q')
# Get some input started, strip it and place in lowercase
all_aboard = input("Hello, friend. Let's play with lists and dictionaries in python 3!"
                   "\nALL ABOARD! Continue? (Yes / No)\n >>> ").lower().strip()
all_aboard_again = None
user_modification = None
print(all_aboard)
# now, lets start the program
if all_aboard is not None:
    # filter bad entries
    #while all_aboard != 'yes' or all_aboard != 'no':
    #    all_aboard = input("Want to try that again, friend? Command not understood.\n"
    #                       "Continue? Yes / No (Spaces and caps do not matter): ").lower().strip()

    if all_aboard == 'yes' and user_modification != 'q':
        # variable for user entered list starts empty
        user_list = []
        # make this a list so stripping is nice and easy
        user_entry = input("Please enter strings and/or numbers separated by commas to be entered in your list."
                           " Spacing is ignored.\nEx: 36, f1d0, happy77. Or add just one, and append away!\n"
                           " >>> ").split(',')
        # strip spaces in the list from entry
        user_values = [i.strip(' ') for i in user_entry]
        user_dict = {}
        user_keys = len(user_values)

        print(user_values)
        print(user_keys)
        user_modification = input("What would you like to do to the list, friend?"
                                  "\nWould you like to (A)ppend, (E)xtend, (I)nsert,"
                                  "(R)emove, Re(V)erse, or (S)ort? Q will quit. \n >>> ").strip().lower()
        while user_modification != 'q':
            #filter out the bad
            while user_modification not in mod_choices:
                user_modification = input("Let's try that again. (A)ppend, (E)xtend, (I)nsert,"
                                          " (R)emove, Re(V)erse, or (S)ort? (Q to quit) \n >>> ").strip().lower()
            if user_modification in mod_choices:
                print(f"{user_modification.upper()} entered...")
                if user_modification == 'a':
                    append = input("Enter the value to be appended. \n >>> ").strip()
                    while append is None or append == 'q':
                        append = input("No value detected. Please enter a value or Q to quit. \n >>> ")
                        if append == 'q':
                            print('*$*' * 4, "EXITING", '*$*' * 4)
                            break
                    user_values.append(append)
                    user_modification = input(f"List updated.\nYour list is now : {user_values}\n"
                                              f"(A)ppend, (E)xtend, (I)nsert, (R)emove, Re(V)erse, or (S)ort?"
                                              f" (Q to quit)\n >>> ").lower().strip()
                elif user_modification == 'e':
                    extend = input("Enter extension value. Commas are required if using multiple values."
                                   " Extend works like x, y, z. Be advised 'q' will quit. \n >>> ")
                    while len(extend) >= 2 and extend.count(',') < 1:
                        # require commas in input
                        extend = input("Multiple values detected without commas, please try again."
                                       " Or, Q to quit. \n >>> ")
                        if extend == ('q', 'Q'):
                            print('*$*' * 4, "EXITING", '*$*' * 4)
                            break
                    # split after to get .count(',') to work
                    extend = extend.split(',')
                    # strip brackets if they are used
                    extend = [e.strip('[] ') for e in extend]
                    # extend the list
                    user_values.extend(extend)
                    print("Your list has been extended by", extend, "Below is your new list.\n", user_values)
                    user_modification = input("What would you like to do to the list, friend?"
                                              "\nWould you like to (A)ppend, (E)xtend, (I)nsert,"
                                              "(R)emove, Re(V)erse, (S)ort or (Q)uit. \n >>> ").strip().lower()
                elif user_modification == 'i':
                    insert = input("Insert chosen! Enter index value (must be an integer) and insert value with"
                                   " commas, ex 0, 'joe'\n >>> ")
                    #index, insert = insert.split(',')
                    #print(len(insert.split(',')), '\n', insert.count(','))
                    print(insert)
                    # require comma separation and only (index, insert)
                    index, xnum = insert.split(',')
                    while type(index) == 'str' and len(insert.split(',')) > 2 and insert.count(',') < 1:
                        insert = input("Bad value detected! Only 2 values. First must be an index number."
                                       " Enter index value and insert value with"
                                       " commas, ex 0, 'joe'. Remember: list.insert(i, x)\n >>> ").strip('() ')



                    print(type(index))
                    user_values.insert(int(index), xnum)

                    print(user_values)
                    user_modification = input("What would you like to do to the list, friend?"
                                              "\nWould you like to (A)ppend, (E)xtend, (I)nsert,"
                                              "(R)emove, Re(V)erse, (S)ort or (Q)uit. \n >>> ").strip().lower()



        user_modification = input("What would you like to do to the list, friend?"
                                  "\nWould you like to (A)ppend, (E)xtend, (I)nsert,"
                                  "(R)emove, Re(V)erse, (S)ort or (Q)uit. \n >>> ").strip().lower()










    elif all_aboard == ('no', 'quit', 'exit') or all_aboard_again == 'no' or user_modification == 'q':
        print('*$*'*4, "EXITING", '*$*'*4)
        # break
    if all_aboard == ('no', 'quit', 'exit'):
        print('*$*'*4, "EXITING", '*$*'*4)
