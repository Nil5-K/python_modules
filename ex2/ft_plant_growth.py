class Plant:
    name = ""
    height = 0.0
    current_age = 0
    growth = 0

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm,"
              f" {self.current_age} days old")

    def grow(self, n):
        self.height = self.height + n
        self.growth += n

    def age(self, n):
        self.current_age = self.current_age + n


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.current_age = 30

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.show()
        rose.grow(0.8)
        rose.age(1)

    print(f"Growth this week: {round(rose.growth)}cm")
