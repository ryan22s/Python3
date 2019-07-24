from operator import itemgetter
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
movies = {"Munich":[2005, "Steven Spielberg"],
                           "The Prestige": [2006, "Christopher Nolan"],
                           "The Departed": [2006, "Martin Scorsese"],
                           "Into the Wild": [2007, "Sean Penn"],
                           "The Dark Knight": [2008, "Christopher Nolan"],
                           "Mary and Max": [2009, "Adam Elliot"],
                           "The King\'s Speech": [2010, "Tom Hooper"],
                           "The Help": [2011, "Tate Taylor"],
                           "The Artist": [2011, "Michel Hazanavicius"],
                           "Argo": [2012, "Ben Affleck"],
                           "12 Years a Slave": [2013, "Steve McQueen"],
                           "Birdman": [2014, "Alejandro G. Inarritu"],
                           "Spotlight": [2015, "Tom McCarthy"],
                           "The BFG": [2016, "Steven Spielberg"]}
menu_check = True
menu_ask = input("Choose an option:\n")
if menu_ask == 'q':
    menu_check = False
elif menu_ask == "t":
    print(2)
    year_dict = {}
    for key, value in sorted(movies.items()):
        print(key, value)

elif menu_ask == 'd':
    for key, value in sorted(movies.items(), key=lambda i: (i[1][1])):
        if value[1] == 'Steven Spielberg' or value[1] == 'Christopher Nolan':
            print(f"{value[1]}:\n\t{key}, {value[0]}\n{value[1]}:\n\t{key}, {value[0]}\n")
        else:
            print(value[1], key, value[0])

elif menu_ask == 'y':
    #for key, value in sorted(movies.items(), key=lambda item: (item[1][0])):
    for key, value in sorted(movies.items(), key=itemgetter(1)):
        title = key
        year = value[0]
        director = value[1]
        o_title = None
        o_dir = None
        w_title = value[1][0]
        w_dir = value[1][1]
        #if year == 2006 or year == 2011:
          #  print(f"{year}:\n\t{o_title}, {o_dir}\n\t{w_title}, {w_dir}\n")
        #elif year != 2006 or year != 2011:
        print(f"{year}:\n\t{title}, {director}\n")

