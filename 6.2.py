import math
print('%s: is a %f dogs in %f cats' % ('Edna', 4.22, 5.222))
# Minimum Field Width, sets it to min of 5 spaces, bob is only 3
# paren to show spaces
print('Student name (%5s)' % 'Bob')
# adding leading zeros on ints
#student_id = int(input('Enter student ID: '))
student_id = 1255
print('The user entered %d' % student_id)
print('Full 8-character student ID: %08d' % student_id)

# floats

real_pi = math.pi  # math library provides close approximation of pi
approximate_pi = 22.0 / 7.0  # Approximate pi to 2 decimal places

print('pi is %f.' % real_pi)
print('22/7 is %f.' % approximate_pi)
# . is just the int. number after dot is number of decimal places
print('22/7 is accurate for 2 decimal places: %.3f' % approximate_pi)


print('%05d' % 150)
print('%05d' % 75.55)
print('%05.1f' % 75.55)
