class Plant:
    name = ""
    height = 0
    age = 0

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.age = 30
    rose.show()

    sunflower = Plant()
    sunflower.name = "Sunflower"
    sunflower.height = 80
    sunflower.age = 45
    sunflower.show()

    cactus = Plant()
    cactus.name = "Cactus"
    cactus.height = 15
    cactus.age = 120
    cactus.show()
