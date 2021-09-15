class Animal:
    def __init__(self, name, age, weight):
        self._name = name
        self._age = age
        self._weight = weight

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, x):
        self._age = x


class Dog(Animal):
    def __init__(self, name, age, weight, color, breed):
        super().__init__(name, age, weight)
        self._color = color
        self._breed = breed

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, x):
        self._color = x

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, x):
        self._breed = x


dog = Dog("Tim", 10, 15, "White", "Husky")
print(dog.age, dog.color, dog.breed)
dog.age, dog.color, dog.breed = 12, "Black", "Pug"
print(dog.age, dog.color, dog.breed)
