from operator import itemgetter
# Build a dictionary containing the specified movie collection
movies = {
    '2005': ['Munich', 'Steven Spielberg'],
    '2006': [['The Prestige', 'Christopher Nolan'], ['The Departed', 'Martin Scorsese']],
    '2007': ['Into the Wild', 'Sean Penn'],
    '2008': ['The Dark Knight', 'Christopher Nolan'],
    '2009': ["Mary and Max", "Adam Elliot"],
    '2010': ["The King's Speech", "Tom Hooper"],
    '2011': [['The Artist', 'Michel Hazanavicius'], ['The Help', 'Tate Taylor']],
    '2012': ['Argo', 'Ben Affleck'],
    '2013': ['12 Years a Slave', 'Steve McQueen'],
    '2014': ['Birdman', 'Alejandro G. Inarritu'],
    '2015': ['Spotlight', 'Tom McCarthy'],
    '2016': ["The BFG", "Steven Spielberg"]
}
dir_dict = {
            'Adam Elliot': ['Mary and Max', 2009],
            'Alejandro G. Inarritu': ['Birdman', 2014],
            'Ben Affleck': ['Argo', 2012],
            'Christopher Nolan': [['The Prestige', 2006], ['The Dark Knight', 2008]],
            'Martin Scorsese': ['The Departed', 2006],
            'Michel Hazanavicius': ['The Artist', 2011],
            'Sean Penn': ['Into the Wild', 2007],
            'Steve McQueen': ['12 Years a Slave', 2013],
            'Steven Spielberg': [['Munich', 2005], ['The BFG', 2016]],
            'Tate Taylor': ['The Help', 2011],
            'Tom Hooper': ["The King's Speech", 2010],
            'Tom McCarthy': ['Spotlight', 2015]
        }
title_dict = {
    "12 Years a Slave": ['Steve McQueen', 2013],
    'Argo': ['Ben Affleck', 2012],
    'Birdman': ['Alejandro G. Inarritu', 2014],
    'Into the Wild': ['Sean Penn', 2007],
    'Mary and Max': ['Adam Elliot', 2009],
    'Munich': ['Steven Spielberg', 2005],
    'Spotlight':['Tom McCarthy', 2015],
    'The Artist': ['Michel Hazanavicius', 2011],
    'The BFG': ['Steven Spielberg', 2016],
    'The Dark Knight': ['Christopher Nolan', 2008],
    'The Departed': ['Martin Scorsese', 2006],
    'The Help': ['Tate Taylor', 2011],
    "The King's Speech": ['Tom Hooper', 2010],
    "The Prestige": ['Chistopher Nolan', 2006]
}
blank_list = []
valencia = True

# Prompt the user for a year
# valencia is my default name for passing
while valencia:
    year_choice = (input("Enter a year between 2005 and 2016:\n"))
    # Displaying the title(s) and directors(s) from that year
    if year_choice not in movies:
        print("N/A")
    else:
        if year_choice == '2011' or year_choice == '2006':
            for keys in movies[year_choice]:
                print(', '.join([str(value) for value in keys]))
        else:
            blank_list.append(movies[year_choice])
            print(', '.join([str(value) for value in movies[year_choice]]))
    valencia = False
menu = "MENU" \
       "\nSort by:" \
       "\ny - Year" \
       "\nd - Director" \
       "\nt - Movie title" \
       "\nq - Quit\n"
user_check = True
menu_space = True
while user_check:
    if menu_space:
        # space needed for initial menu formatting.
        print()
        menu_space = False
    # Display menu
    print(menu)
    menu_ask = input("Choose an option:\n")
    if menu_ask == 'q':
        user_check = False
    # Carry out the desired option: Display movies by year
    elif menu_ask == "y":
        for key, value in sorted(movies.items()):
            year = int(key)
            title = value[0]
            director = value[1]
            o_title = value[0][0]
            o_dir = value[0][1]
            w_title = value[1][0]
            w_dir = value[1][1]
            if year == 2006 or year == 2011:
                print(f"{year}:\n\t{o_title}, {o_dir}\n\t{w_title}, {w_dir}\n")
            elif year != 2006 or year != 2011:
                print(f"{year}:\n\t{title}, {director}\n")
    elif menu_ask == 'd':
        # neither lambda or itemgrabber will sort with lists
        for key, value in sorted(dir_dict.items()):
            director = key
            title = value[0]
            year = value[1]

            if director == 'Steven Spielberg':
                print(f"{director}:\n\t{value[0][0]}, {value[0][1]}\n"
                      f"\t{value[1][0]}, {value[1][1]}\n")
            elif director == 'Christopher Nolan':
                print(f"{director}:\n\t{value[0][0]}, {value[0][1]}\n"
                      f"\t{value[1][0]}, {value[1][1]}\n")
            else:
                print(f"{director}:\n\t{title}, {year}\n")
    elif menu_ask == 't':
        for key, value in sorted(title_dict.items()):
            title = key
            director = value[0]
            year = value[1]
            print(f"{title}:\n\t{director}, {year}\n")
    else:
        try:
            int(input("hi:>>> "))
        except ValueError:
            print('This was a pain in the ass with lists. ')










    # display movies by director, display movies by movie title, or quit
