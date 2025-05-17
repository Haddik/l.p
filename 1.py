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

Student = StudentCL("Artem", 1132242346, [4, 3, 4, 4, 5])
#Student.display_info()
Student.addgrade(6)
Student.display_info()