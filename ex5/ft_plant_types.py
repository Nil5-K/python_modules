class Plant:
    _growth = 0

    def __init__(self, name, height, current_age):
        self.name = name
        self._height = height
        self._current_age = current_age

    def show(self):
        return (f"{self.name}: {round(self._height, 1)}cm,"
                f" {self._current_age} days old")

    def grow(self, n):
        self._height = self._height + n
        self._growth += n

    def age(self, n):
        self._current_age = self._current_age + n

    def set_height(self, new_height):
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative\n" +
                  "Height update rejected")
            return
        self._height = new_height

    def set_age(self, new_age):
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative\n" +
                  "Age update rejected")
            return
        self._current_age = new_age

    def get_age(self):
        return self._current_age

    def get_height(self):
        return self._height


class Flower(Plant):
	def __init__(self, name, height, age, color):
		super(name, height, age)
		self.color = color
