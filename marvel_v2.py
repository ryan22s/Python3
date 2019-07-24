# GLOBALS needed for functions
mcu = {
    2008: ["Iron Man", 'The Incredible Hulk'],
    2010: ["Iron Man 2"],
    2011: ["Thor", "Captain America: The First Avenger"],
    2012: ["Marvel's The Avengers"],
    2013: ['Iron Man 3', 'Thor: The Dark World'],
    2014: ['Captain America: The Winter Soldier', "Guardians of the Galaxy"],
    2015: ["Avengers: Age of Ultron", "Ant-Man"],
    2016: ['Captain America: Civil War', "Doctor Strange"],
    2017: ['Guardians of the Galaxy Vol. 2', 'Spider-Man: Homecoming', 'Thor: Ragnarok'],
    2018: ['Black Panther', 'Avengers: Infinity War', 'Ant-Man and the Wasp']
}
# empty dict for later copying
mcu_temp = {}


def captain_america():
    """
    Captain America is very old fashioned! Non-valid input is not tolerated!
    :return this returns an error message when invalid input is entered:
    """
    saying = "Language! --Captain America"
    return saying


def param_ex(arg):
    """ Using param to return arg value for error handling"""
    return arg


def entry_func():
    """
    Entrance function. Title. Error handling.
    :return nada. Nothing is returned:
    """

    first_time = True
    while first_time:
        try:
            print("""
            ************************************************************************************************************
            ************************************************************************************************************
                                                    MARVEL CINEMATIC UNIVERSE
            ************************************************************************************************************
            ************************************************************************************************************
            """)
            first_entry = int(input("Enter a year from 2008 to 2018\n >>> "))
        except ValueError:
            print(captain_america(), '\n')
            break
        if first_entry not in mcu:
            print(param_ex(first_entry), "N/A")
            pass
        else:
            for key, value in mcu.items():
                if first_entry == key:
                    if len(value) == 3:
                        print(f"{key}:\n\t{value[0]}\n\t{value[1]}\n\t{value[2]}\n")
                    elif len(value) == 2:
                        print(f"{key}:\n\t{value[0]}\n\t{value[1]}\n")
                    else:
                        print(f"{key}:\n\t{value[0]}\n")
        # formatting space
        print()
        # exit intro
        first_time = False


def main():
    # import globals for write access
    global mcu_temp
    # Start this up
    entry_func()
    # Then, run main()
    menu = "Marvel Cinematic Universe Movie Sorter v1.0" \
        "\n****Current up to August 2018****" \
        "\nSort by:" \
        "\ny - Year" \
        "\nt - Movie title" \
        "\nq - Quit\n"
    menu_prompt = True
    while menu_prompt:
        print(menu)
        menu_entry = input("Sort by choice:\n >>> ")
        if menu_entry == 'q':
            menu_prompt = False
        elif menu_entry == 't':
            mcu_temp = {}
            for key, value in mcu.items():
                # get sorted ready! We're coming in for landing soon
                if len(value) == 3:
                    # keep original dict order for multi-release title years
                    mcu_temp[value[0]] = key
                    mcu_temp[value[1]] = key
                    mcu_temp[value[2]] = key
                elif len(value) == 2:
                    mcu_temp[value[0]] = key
                    mcu_temp[value[1]] = key
                else:
                    mcu_temp[value[0]] = key
            for key, value in sorted(mcu_temp.items()):
                print(f"{key}, {value}\n")
        elif menu_entry == 'y':
            mcu_temp = {}
            for key, value in mcu.items():
                if key not in mcu_temp:
                    if len(value) == 3:
                        mcu_temp[key] = [value[0], value[1], value[2]]
                    elif len(value) == 2:
                        mcu_temp[key] = [value[0], value[1]]
                    else:
                        mcu_temp[key] = [value[0]]
            for key, value in sorted(mcu_temp.items()):
                value = '\n\t'.join(value)
                print(f"{key}:\n\t{value}\n")
        else:
            print(captain_america(), '\n')


main()
