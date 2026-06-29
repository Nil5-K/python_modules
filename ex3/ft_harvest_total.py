def ft_harvest_total():
    sum = 0
    i = 1
    while i < 4:
        sum += int(input(f"Day {i} harvest: "))
        i += 1
    print(f"Total harvest: {sum}")
