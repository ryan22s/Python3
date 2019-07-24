hourly_temperature = [90, 92, 94, 95]

for ele in hourly_temperature:
    if ele == hourly_temperature[-1]:
        print(ele, end=" \n")
    else:
        # flush negates newline, no spaces
        print(ele, end=" -> ", flush=True)
