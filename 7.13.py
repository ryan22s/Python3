weight = []
i = 1
while i < 5:
    entered_weight = float(input(f"Enter weight {i}: \n"))
    weight.append(entered_weight)
    i += 1
print("\nWeights:", weight)
avg_weight = sum(weight) / len(weight)
print("Average weight:", avg_weight)
print("\nMax weight:", max(weight))
ind_list = int(input("\nEnter a list index (1 - 4): \n"))
ind_list -= 1
print(f"Weight in pounds: {weight[ind_list]}\nWeight in kilograms:{weight[ind_list]/2.2}\n")
print(f"\nSort list: {sorted(weight)}")

