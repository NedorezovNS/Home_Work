class Student:
    list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.list.append(self)

    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'

    def average_score(self):
        average_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            average_of_course = course_sum / len(course_grades)
            average_sum += average_of_course
        if average_sum == 0:
            return f'Студент еще не получал оценки'
        else:
            return f'{average_sum / len(self.grades.values()):.2f}'

    def __str__(self):
        res = (f'Имя: {self.name} \nФамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {self.average_score()}\n'
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {", ".join(self.finished_courses)} \n')
        return res

    def __lt__(self, student):
        if isinstance(student, Student):
            return self.average_score() < student.average_score()

    def __le__(self, student):
        if isinstance(student, Student):
            return self.average_score() <= student.average_score()

    def __eq__(self, student):
        if isinstance(student, Student):
            return self.average_score() == student.average_score()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.rates = {}


class Lecturer(Mentor):
    list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        Lecturer.list.append(self)

    def average_rate(self):
        average_sum = 0
        for course_grades in self.rates.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            average_of_course = course_sum / len(course_grades)
            average_sum += average_of_course
        if average_sum == 0:
            return f'Лектору еще не выставляли оценки'
        else:
            return f'{average_sum / len(self.rates.values()):.2f}'

    def __str__(self):
        res = (f'Имя: {self.name} \nФамилия: {self.surname}\n'
               f'Средняя оценка {self.average_rate()}\n')
        return res

    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.average_rate() < lecturer.average_rate()

    def __le__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.average_rate() <= lecturer.average_rate()

    def __eq__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.average_rate() == lecturer.average_rate()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        return res


def grades_students(student_list, course):
    overall_student_rating = 0
    lectors = 0
    for listener in student_list:
        if course in listener.grades.keys():
            average_student_score = 0
            for grades in listener.grades[course]:
                average_student_score += grades
            overall_student_rating = average_student_score / len(listener.grades[course])
            average_student_score += overall_student_rating
            lectors += 1
    if overall_student_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{overall_student_rating / lectors:.2f}'


def grades_lecturers(lecturer_list, course):
    average_rating = 0
    b = 0
    for lecturer in lecturer_list:
        if course in lecturer.rates.keys():
            lecturer_average_rates = 0
            for rate in lecturer.rates[course]:
                lecturer_average_rates += rate
            overall_lecturer_average_rates = lecturer_average_rates / len(lecturer.rates[course])
            average_rating += overall_lecturer_average_rates
            b += 1
    if average_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{average_rating / b:.2f}'


student_1 = Student('Дмитрий', 'Соколов', 'Male')
student_1.finished_courses = ['Basic', 'C#']
student_1.courses_in_progress = ['Git', 'Java']

student_2 = Student('Сергей', 'Дроздов', 'Male')
student_2.finished_courses = ['Pascal', 'Git']
student_2.courses_in_progress = ['Python', 'Java']

student_3 = Student('Пётр', 'Лебедев', 'Helicopter')
student_3.finished_courses = ['C', 'C#']
student_3.courses_in_progress = ['Python']

lecturer_1 = Lecturer('Игорь', 'Воробьев')
lecturer_1.courses_attached = ['Git', 'Java']

lecturer_2 = Lecturer('Василий', 'Орлов')
lecturer_2.courses_attached = ['Python']

reviewer_1 = Reviewer('Андрей', 'Воронин')
reviewer_1.courses_attached = ['Basic', 'С#', 'Java', 'Git']

reviewer_2 = Reviewer('Геннадий', 'Голубев')
reviewer_2.courses_attached = ['Git', 'Python', 'Pascal']

reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_1, 'Git', 7)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Java', 5)
reviewer_1.rate_hw(student_1, 'Java', 8)
reviewer_1.rate_hw(student_1, 'Java', 9)
reviewer_1.rate_hw(student_1, 'Basic', 9)
reviewer_1.rate_hw(student_1, 'Basic', 3)
reviewer_1.rate_hw(student_1, 'Basic', 2)
reviewer_1.rate_hw(student_1, 'С#', 10)
reviewer_1.rate_hw(student_1, 'С#', 9)
reviewer_1.rate_hw(student_1, 'С#', 4)

reviewer_2.rate_hw(student_2, 'С++', 4)
reviewer_2.rate_hw(student_2, 'С++', 2)
reviewer_2.rate_hw(student_2, 'С++', 3)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 1)
reviewer_2.rate_hw(student_2, 'Git', 7)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 5)

reviewer_2.rate_hw(student_3, 'Python', 8)
reviewer_2.rate_hw(student_3, 'Python', 8)
reviewer_2.rate_hw(student_3, 'Python', 8)


student_1.rate_lecturer(lecturer_1, 'Git', 10)
student_1.rate_lecturer(lecturer_1, 'Git', 5)
student_1.rate_lecturer(lecturer_1, 'Git', 9)
student_1.rate_lecturer(lecturer_1, 'Java', 6)
student_1.rate_lecturer(lecturer_1, 'Java', 7)
student_1.rate_lecturer(lecturer_1, 'Java', 8)

student_2.rate_lecturer(lecturer_1, 'Java', 10)
student_2.rate_lecturer(lecturer_1, 'Java', 9)
student_2.rate_lecturer(lecturer_1, 'Java', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 2)
student_2.rate_lecturer(lecturer_2, 'Python', 8)

print(student_1)
print(student_2)
print(student_3)

if student_1 > student_2:
    print(f'{student_1.name} учится лучше, чем {student_2.name} \n')
else:
    print(f'{student_2.name} учится лучше, чем {student_1.name} \n')

if student_1 == student_3:
    print(f'{student_1.name} и {student_3.name} имеют одинаковый средний балл\n')
else:
    print(f'{student_1.name} и {student_2.name} имеют разный средний балл\n')

print(reviewer_1)
print(reviewer_2)

print(lecturer_1)
print(lecturer_2)

if lecturer_1 > lecturer_2:
    print(f'{lecturer_1.name} {lecturer_1.surname} преподает лучше, чем {lecturer_2.name} {lecturer_2.surname} \n')
else:
    print(f'{lecturer_2.name} {lecturer_2.surname} преподает лучше, чем {lecturer_1.name} {lecturer_1.surname} \n')

print(f'Средняя оценка студентов по курсу "Git": {grades_students(Student.list, "Git")}')
print(f'Средняя оценка студентов по курсу "Java": {grades_students(Student.list, "Java")}')
print(f'Средняя оценка студентов по курсу "Python": {grades_students(Student.list, "Python")}')
print('')
print(f'Средняя оценка лекторов по курсу "Git": {grades_lecturers(Lecturer.list, "Git")}')
print(f'Средняя оценка лекторов по курсу "Java": {grades_lecturers(Lecturer.list, "Java")}')
print(f'Средняя оценка лекторов по курсу "Python": {grades_lecturers(Lecturer.list, "Python")}')
