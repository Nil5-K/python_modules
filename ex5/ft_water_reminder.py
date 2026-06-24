def ft_water_reminder():
    user_input = int(input("Days since last watering: "))
    if user_input > 2:
        print("Water the plants!")
    else:
        print("Plants are fine.")
