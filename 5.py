class StudentCL():
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def addgrade(self, grade):
        if grade > 0 < 10:
            self.grades.append(grade)
    def getaverage(self):
        return sum(self.grades)/2
    def display_info(self):
        print("Имя: " + self.name + "\nID студента: " +
        str(self.student_id) + "\nБаллы студента: " + str(self.grades)
        + "\nСредний балл студента: " + str(self.getaverage()))

    def __str__(self):
            return f"Студент: {self.name} (ID: {self.student_id}), Средний балл: {self.getaverage():.2f}"
    def __eq__(self, other):
            if isinstance(other, StudentCL):
                return self.student_id == other.student_id
            return False
    def __len__(self):
            return len(self.grades)

student1 = StudentCL("Артем Тульбович", 123, [5, 8, 7])
student2 = StudentCL("Иван Ургант", 124, [9, 8, 10])
student3 = StudentCL("Алексей Щербаков", 123, [6, 7, 8])

        # Тестируем __str__
print(student1)
print(student2)

        # Тестируем __eq__
print(student1 == student2)
print(student1 == student3)
print(student1 == "не студент")

        # Тестируем __len__
print('Колличество оценок: ',len(student1))
student1.addgrade(9)
print('Колличество оценок: ',len(student1))