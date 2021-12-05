class Student:
    def __init__(self, name, surname, gender, avg_grade, courses_in_progress, finished_courses):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grade = avg_grade

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

        else:
            return 'Error'

    def __str__(self):
        self.courses_in_progress = 'Python, Git'
        self.finished_courses = 'Введение в программирование'
        res_st = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade}\n' \
                 f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res_st

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.avg_grade < other.avg_grade


class Mentors:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentors):
    def __init__(self, name, surname, avg_grade):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_grade = avg_grade

    def __str__(self):
        res_lec = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade}'
        return res_lec

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.avg_grade < other.avg_grade


class Reviewer(Mentors):
    def rate_st(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

        else:
            return 'Error'

    def __str__(self):
        res_rev = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res_rev


best_student = Student('Ruoy', 'Eman', 'your_gender', 'Python, Git', 'Введение в программирование', 9.9)
best_student.courses_in_progress += ['Python', 'Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_st(best_student, 'Python', 10)
cool_reviewer.rate_st(best_student, 'Python', 10)
cool_reviewer.rate_st(best_student, 'Python', 10)

print(best_student.grades)

best_lecturer = Lecturer('Some', 'Buddy', 9.9)
best_lecturer.courses_attached += ['Python']

cool_student = Student('Ruoy', 'Eman', 'your_gender', 'Python, Git', 'Введение в программирование', 9.9)
cool_student.courses_in_progress += ['Python', 'Git']

cool_student.rate_lec(best_lecturer, 'Python', 10)
cool_student.rate_lec(best_lecturer, 'Python', 10)
cool_student.rate_lec(best_lecturer, 'Python', 10)

print(best_lecturer.grades)
print()

some_reviewers = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy', 9.9)
some_student = Student('Ruoy', 'Eman', 'your_gender', 9.9, 'Python, Git', 'Введение в программирование')
print(some_reviewers)
print()
print(some_lecturer)
print()
print(some_student)
print()

ruoy_eman = Student('Ruoy', 'Eman', 'your_gender', 9.9, 'Python', 'Введение в программирование')
max_bolt = Student('Max', 'Bolt', 'your_gender', 9.5, 'Python', 'Введение в программирование')
print(ruoy_eman < max_bolt)

john_smith = Lecturer('John', 'Smith', 10)
mike_tyson = Lecturer('Mike', 'Tyson', 5)
print(john_smith > mike_tyson)


class Student:
    def __init__(self, name, surname, gender, avg_grade, courses_in_progress, finished_courses):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = finished_courses
        self.courses_in_progress = courses_in_progress
        self.grades = {}
        self.avg_grade = avg_grade

    def __str__(self):
        res = f'Имя = {self.name}, Фамилия = {self.surname}, Пол = {self.gender}, Средняя оценка = {self.avg_grade},' \
              f'Курсы в процессе изучения = {self.courses_in_progress}, Оконченные курсы = {self.finished_courses}'
        return res


ruoy_eman = Student('Ruoy', 'Eman', 'male', 9.9, 'Python', 'Введение в программирование')
print(ruoy_eman)


class Mentors:
    def __init__(self, name, surname, courses_attached):
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached

    def __str__(self):
        res = f'Имя = {self.name}, Фамилия = {self.surname}, Закреплённые курсы = {self.courses_attached}'
        return res

john_smith = Mentors('John', 'Smith', 'Python')
print(john_smith)

some_students = [
  {'name': 'First Student', 'course': 'Python', 'grades': [9, 10, 9, 6]},
  {'name': 'Second Student', 'course': 'Python', 'grades': [9, 10, 9]},
  {'name': 'Third Student', 'course': 'Git', 'grades': [9, 10, 9]},
  {'name': 'Fourth Student', 'course': 'Git', 'grades': [9, 10, 9, 7]},
]

def avg_grades(students, courses=None):
  sum_grades = 0
  count = 0
  for student in students:
    if student['course'] == courses or courses is None:
      sum_grades += sum(student['grades']) / len(student['grades'])
      count += 1
  return round((sum_grades / count), 2)

print(avg_grades(some_students, 'Git'))
print(avg_grades(some_students, 'Python'))
print(avg_grades(some_students))


some_mentors = [
  {'name': 'First Mentor', 'course_attached': 'Python', 'grades': [10, 10, 9, 6]},
  {'name': 'Second Mentor', 'course_attached': 'Python', 'grades': [6, 8, 10, 9]},
  {'name': 'Third Mentor', 'course_attached': 'Git', 'grades': [9, 9, 10, 9]},
  {'name': 'Fourth Mentor', 'course_attached': 'Git', 'grades': [9, 10, 9, 7]},
]



def avg_grades(mentors, courses=None):
  sum_grades = 0
  count = 0
  for mentor in mentors:
    if mentor['course_attached'] == courses or courses is None:
      sum_grades += sum(mentor['grades']) / len(mentor['grades'])
      count += 1
  return round((sum_grades / count), 2)

print(avg_grades(some_mentors, 'Git'))
print(avg_grades(some_mentors, 'Python'))
print(avg_grades(some_mentors))