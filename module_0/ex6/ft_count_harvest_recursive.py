def count_up(n):
    if n <= 0:
        return
    else:
        count_up(n - 1)
        print(f"Day {n}")


def ft_count_harvest_recursive():
    count_up(int(input("Days until harvest: ")))
    print("Harvest time!")
