def main():
    movieCollectionDict = {"Munich":[2005, "Steven Spielberg"],
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
    promptForYear = True
    while promptForYear:
        yearChoice = int(input("Enter a year between 2005 and 2016:\n"))
        if yearChoice<2005 or yearChoice>2016:
            print("N/A")
        else:
            for key, value in movieCollectionDict.items():
                if value[0] == yearChoice:
                    print(key + ", boner " + str(value[1]))
            promptForYear = False
    menu = "MENU" \
           "\nSort by:" \
           "\ny - Year" \
           "\nd - Director" \
           "\nt - Movie title" \
           "\nq - Quit\n"
    promptUser = True
    first_time = True
    while promptUser:
        if first_time is True:
            print()
            first_time = False
        print(menu)
        userChoice = input("Choose an option:\n")
        if userChoice == "q":
            promptUser = False
        elif userChoice=="y":
            year_sorted = {}
            for key, value in sorted(movieCollectionDict.items(), key=lambda item: (item[0], item[1])):
                year = value[0]
                title = key
                director = value[1]
                if year not in year_sorted:
                    year_sorted[year] = [[title, director]]
                else:
                    year_sorted[year].append([title, director])
            for year in sorted(year_sorted):
                print (year,end=':\n')
                movies = year_sorted[year]
                for movie in sorted(movies, key = lambda x:x[0]):
                    print("\t"+movie[0] + ", " + movie[1])
                print()
        elif userChoice == "d":
            director_sorted = {}
            for key, value in sorted(movieCollectionDict.items(), key=lambda item: (item[1][1])):
                year = value[0]
                title = key
                director = value[1]
                if director not in director_sorted:
                    director_sorted[director] = [[title, year]]
                else:
                    director_sorted[director].append([title, year])
            for director in sorted(director_sorted):
                print (director,end=':\n')
                movies = director_sorted[director]
                for movie in sorted(movies, key = lambda x:x[0]):
                    print("\t"+movie[0] + ", " + str(movie[1]))
                print()
        elif userChoice == "t":
            for key, value in sorted(movieCollectionDict.items(), key=lambda item: (item[0], item[1])):
                print(key,end=':\n')
                print("\t" + str(value[1]) + ", " + str(value[0])+"\n")
        else:
            print("Invalid input")

main()
