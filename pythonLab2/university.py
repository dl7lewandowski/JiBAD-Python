class Person:

    def __init__(self, first_name, last_name, mail):
        self.first_name = first_name
        self.last_name = last_name
        self.mail = mail
        self.inbox = dict()

    def send_email(self, author, message):
        self.inbox[author] = message
        print("Tresc wiadmości: \"{}\", Wysłana na mail: \"{}\"".format(message, self.mail))

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.mail


# Student
class Student(Person):
    def __init__(self, first_name, last_name, mail, number_index, grades):
        Person.__init__(self, first_name, last_name, mail)
        self.number_index = number_index
        self.grades = grades

    def add_grade(self, subject, grade):
        self.grades[subject].append(grade)

    def __str__(self):
        return Person.__str__(self) + " " + str(self.number_index) + " " + str(self.grades)



# Pracnownik
class Employee(Person):

    def __init__(self, first_name, last_name, mail, number_room):
        Person.__init__(self,first_name, last_name, mail)
        self.number_room = number_room

    def __str__(self):
        return Person.__str__(self) + " " + self.number_room


# Pracownik naukowy
class Scientist(Employee):

    def __init__(self, first_name, last_name, mail, number_room, publications):
        Employee.__init__(self, first_name, last_name, mail, number_room)
        self.publications = publications

    def add_publications(self, publications):
        self.publications.append(publications)

    def __str__(self):
        return Employee.__str__(self) + " " + str(self.publications)


# Pracownik dydaktyczny
class Teacher(Employee):
    def __init__(self, first_name, last_name, mail, number_room, subjects, hour_consultation):
        Employee.__init__(self, first_name, last_name, mail, number_room)
        self.subjects = subjects
        self.hour_consultation = hour_consultation

    def __str__(self):
        return Employee.__str__(self) + " " + str(self.subjects) + " " + self.hour_consultation


if __name__ == "__main__":
    teacher = Teacher("imie", "nazwisko", "mail@", "102", ["Matamatyka", "Angielski"], "Wtorek 12:00")
    print(teacher)
    scientist = Scientist("imie", "nazwisko", "mail@", "203", ["publikacja1","publikacja2"])
    print(scientist)
    student = Student("imie,", "nazwisko", "mail@", "4234", "5")
    print(student)
    student.send_email("student1", "wiadomosc :)")







