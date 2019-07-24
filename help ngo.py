print('Welcome To The Fruit Market')

fruit_list = ['Banana', 'Apple', 'Watermelon', 'Pear', 'Orange', 'Avocado', 'Mango']

for fruit in fruit_list:

    print(fruit)

user_interested = True
inventory = {'banana': '430', 'apple': '220', 'watermelon': '117', 'pear': '315',
             'orange': '286', 'avocado': '570', 'mango': '882'}

menu = ', '.join(fruit_list)
while user_interested:
    print(menu, '\n\tN to quit.')
    result = input('Pick a fruit from the above list to see its availability: ')
    if result == 'N':
        print('Thanks for shopping with us. Come back soon...')
        user_interested = False
    elif result in inventory:
        print(result, ':', inventory[result], '\n')

