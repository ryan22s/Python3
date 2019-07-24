x = {'one': ['one', 'uno'], 'two': ['two', 'dos']}
i = 0
#for keys in x.keys():
    #print(keys, x[keys][1], end=" ")
    #i += 1
for keys, values in x.items():
    print(values, end=" ")
print()
