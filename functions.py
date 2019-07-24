def shampoo_instructions(cycles):
    i = 1
    if cycles < 1:
        print('Too few.')
    elif cycles > 4:
        print('Too many.')
    else:
        while i <= cycles:
            print(f"{i} : Lather and rinse.")
            i += 1

        print("Done.")


shampoo_instructions(3)
