time_entered = int(input("Please enter military time to be translated to standard AM/PM: \n"))
minutes = time_entered % 100
while time_entered >= 2400 or time_entered < 0 or minutes >= 60:
    time_entered = int(input("Let's try that again. Enter military time hours 0 - 23 and minutes 0 - 60: "))
    minutes = time_entered % 100
if 0 <= time_entered <= 1259:
    hours = time_entered // 100
    if hours == 0:
        hours = 12
    if minutes <= 9:
            minutes = str(0) + str(minutes)
    if time_entered <= 1159:
        print(f"It's {hours}:{minutes} AM \n")
    elif time_entered >= 1200:
        print(f"It's {hours}:{minutes} PM.\n")
if 1300 <= time_entered <= 2359:
    hours = (time_entered - 1200) // 100
    minutes = time_entered % 100
    if minutes <= 9:
        minutes = str(0) + str(minutes)
    print(f"It's {hours}:{minutes} pm.\n")
