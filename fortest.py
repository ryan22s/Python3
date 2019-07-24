test_table = [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]
for x in test_table:
    print(' , '.join([str(o) for o in x]))
#for rows in test_table:
    # The join() joins the given elements into one string, using " | " as the separator.
    #  So for three in a row, it only uses two separators.
    # So, join the cell and it will join them together 3 goes to 2
   # print(" | ".join([str(cells) for cells in rows]))
    #print()
print(" | ".join([str(cells) for rows in test_table for cells in rows]))
print([str(cells) for rows in test_table for cells in rows])

#It helps to think of it like this.

#for branch in tree:
 #   for leaf in branch:
  #      yield leaf
