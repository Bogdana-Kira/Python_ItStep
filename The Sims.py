# sims/human.py
class Human:
    def __init__(self, name: str = "Sim", age: int = 0, energy: int = 100, happiness: int = 100, hunger: int = 0):
        """Конструктор класу Human."""
        self.name = name
        self.age = age
        self.energy = energy
        self.happiness = happiness
        self.hunger = hunger

    def eat(self, food: int) -> None:
        """Метод для зміни рівня голоду."""
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0

    def sleep(self, hours: int) -> None:
        """Метод для зміни рівня енергії."""
        self.energy += hours
        if self.energy > 100:
            self.energy = 100

    def play(self, activity: int) -> None:
        """Метод для зміни рівня щастя."""
        self.happiness += activity
        if self.happiness > 100:
            self.happiness = 100

    def age_up(self, years: int = 1) -> None:
        """Метод для зміни віку."""
        self.age += years

    def status(self) -> None:
        """Метод для відображення статусу персонажа."""
        print(f"{self.name}'s Status - Age: {self.age}, Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
# Створення об'єкта типу Human
sim1 = Human("Sim1")

# Виклик методів для симуляції дій персонажа
sim1.eat(30)
sim1.sleep(8)
sim1.play(20)
sim1.age_up(5)

# Виведення статусу персонажа
sim1.status()