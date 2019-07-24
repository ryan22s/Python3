test_grades = [101, 83, 107, 90]
sum_extra = 0#-999  # Initialize 0 before your loop
for num in test_grades:
    #sum_extra = 0
    if num > 100:
        sum_extra += (num - 100)

print('Sum extra:', sum_extra)
