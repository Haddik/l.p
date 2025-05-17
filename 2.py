class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student(name='{self.name}', age={self.age}"

class Teacher(Person):
    def __init__(self, name, age, subject, students=None):
        super().__init__(name, age)
        self.subject = subject
        self.students = students if students is not None else []
    def add_student(self, student: Person):
        self.students.append(student)
    def remove_student(self, student: Person):
         self.students.remove(student)
    def list_students(self):
        return self.students


teacher = Teacher("Ivan", 17, "Programming")
student1 = Person("Artem", 14)
student2 = Person("Roma", 16)

teacher.add_student(student1)
teacher.add_student(student2)

print('Список студентов:')
for student in teacher.list_students():
    print(student)

teacher.remove_student(student2)

print('\n','Новый список студентов:')
for student in teacher.list_students():
    print(student)