def ft_plant_age():
    user_input = int(input("Enter plant age in days: "))
    if user_input > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
