class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} щось каже"


class Dog(Animal):
    def bark(self):
        return f"{self.name} голосно гавкає"


class BreedDog(Animal):  # Використовуйте інше ім'я, щоб уникнути конфлікту
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        # Викликаємо метод speak з батьківського класу
        return f"{super().speak()} і {self.name} є {self.breed}"


# Приклад використання:

animal = Animal("Тварина")
print(animal.speak())  # Виведе: Тварина щось каже

dog = Dog("Собака")
print(dog.speak())    # Виведе: Собака щось каже
print(dog.bark())     # Виведе: Собака голосно гавкає

breed_dog = BreedDog("Собака", "Дог")
print(breed_dog.speak())  # Виведе: Собака щось каже і Собака є Дог
