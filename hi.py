x = {
    'one': ['one', 'uno'],
    'two': ['two', 'dos']
}
for values_one, values_two in x.values():
    print(values_one, values_two, end=" ")

for key, value in x.items():
    for inner in value:
        print(inner, end=" ")

for key in x:
    for value in key:
        print(value, end=" ")
