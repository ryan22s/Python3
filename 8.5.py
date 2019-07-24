size = 6

def get_numbers(num):
    numbers = []
    user_input = input('Enter %s integers:\n' % num)

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers


def print_all_numbers(numbers):
    for numd in numbers:
        print(numd[1], flush=True)


def print_odd_numbers(numbers):
    [print('Odd numbers:', numd,) for numd in numbers if numd % 2 !=0]


def print_negative_numbers(numbers):
    # Print all negative numbers
    print('Negative numbers:')

nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)
