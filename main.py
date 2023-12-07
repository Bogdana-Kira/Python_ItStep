class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self, hours):
        self.grade += hours * 0.1

    def play(self, hours):
        self.grade -= hours * 0.05

    def get_grade(self):
        return self.grade


# Створіть студента
student = Student("Вася", 8)

# Навчіть студента
lesson = float(input("Навчіть студента - "))
student.study(lesson)

# Пограйте з студентом
game = float(input("Пограйте з студентом - "))
student.play(game)

# Отримайте оцінку студента
grade = student.get_grade()

# Виведіть оцінку студента
print(f"Оцінка студента {student.name}: {grade}")
