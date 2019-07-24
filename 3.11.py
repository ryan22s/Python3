from math import ceil


def wall_area(height=1.0, width=1.0):
    calc_area = height * width
    paint = calc_area / 350
    cans_needed = ceil(paint)
    return calc_area, paint, cans_needed


# Dictionary of paint colors and cost per gallon
paintColors = {
    'red': 35,
    'blue': 25,
    'green': 23,
    'purple': 46,
    
}
# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
try:

    wallHeight = float(input('Enter wall height (feet): \n'))
    wallWidth = float(input("Enter wall width (feet): "))
except ValueError:
    wallWidth = 1
    wallHeight = 1

area, paint_needed, cans = wall_area(wallHeight, wallWidth)
print('Wall area:', area, 'square feet')

# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall
print('Paint needed:', paint_needed, 'gallons')
print("Cans needed:", ceil(paint_needed), "can(s)\n")
colorPicked = str(input("Choose a color to paint the wall: \n"))
for key, value in paintColors.items():
    if colorPicked == key:
        print("Cost of Purchasing", key, f"paint: ${value*cans}")
costPaint = paintColors[colorPicked]
