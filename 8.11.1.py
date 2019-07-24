def number_of_pennies(x, y=0):
    """
    Write a function number_of_pennies() that returns the total number of pennies given a number of dollars
    and (optionally) a number of pennies. Ex: 5 dollars and 6 pennies returns 506.
    """
    return x*100+y


print(number_of_pennies(5, 6))  # Should print 506
print(number_of_pennies(4))    # Should print 400
