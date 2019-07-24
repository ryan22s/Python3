def get_num_of_characters(inputStr):
    count = 0
    for text in inputStr.strip(" "):
        count += 1
    return count


def entry_with_no_whitespace(entry):
    balls = entry.replace(" ", "")
    return balls


if __name__ == '__main__':
    easy = input("Enter a sentence or phrase: ")
    print("\nYou entered:", easy)
    friend = get_num_of_characters(easy.strip(" "))
    print("\nNumber of characters:", friend)
    print("String with no whitespace:", entry_with_no_whitespace(easy))
