from student import Student


class Classroom:
    '''class of classroom object that will be populated with students

    Each classroom object has the following attributes:

    _____Attributes_______

        students_array: Array. Contains all students of class Student

        teacher_name: String. Contains the name of the teacher

        classroom_name: String. Contains the name of the class


    _____Methods________

        __init__(self, name):
            Requires the teacher's name passed as a string.
            Requires the classroom name passed as a string.

        create_student(self):
            Ask for input for student_name
            Creates personal student_ID
            Adds student_name to students_array

        add_assignment_student(self)
            ask for student name
            assignment = get_assignment_name(student)
            Ask for input on grade
                Check if grade is in range 1-100
                    If False ask for new input
                    If yes add assignment to student

        add_assignment_classroom(self):
            assignment = get_assignment_name()
            Runs through all the students in students_array
                Ask for input on grade
                    Check if grade is in range 1-100
                        If False ask for new input
                        If yes add assignment to student

        edit_student(self):
            input student name
            get_assignment_name_student(student)


        delete_assignment_classroom(self):
            Input assignment name
            Run through student array
                Check if assignment is in assignments dictionary
                    Remove assigment

        delete_assignment_student(self):
            Input assignment name
            Check if assignment is in assignments dictionary
                Remove assigment'''

    def __init__(self, classroom_name, teacher_name):
        self.classroom_name = classroom_name
        self.teacher_name = teacher_name
        self.roster = {}
        self.student_ID_count = 0
        self.classroom_gpa = 0

    def create_student(self, student_name):
        for student in self.roster.values():
            if student_name in student.name:
                print("Student already exists.")
                return()
        self.student_ID_count += 1
        print("New student id:", self.student_ID_count)
        current_student = Student(student_name, self.student_ID_count)
        self.roster[current_student.student_ID] = current_student

    def add_assignment_student(self, current_student, assignment_name, grade):
        for student in self.roster.values():
            if student.name == current_student:
                if assignment_name not in student.assignments.values():
                    student.add_assignment(assignment_name, grade)
                    print("assignment added")
                    return()

    def add_assignment_classroom(self, assignment_name, grade):
        for student in self.roster.values():
            if assignment_name not in student.assignments.values():
                student.add_assignment(assignment_name, grade)
                print("assignment added")

    def delete_assignment_student(self, current_student, assignment_name):
        for student in self.roster.values():
            if student.name == current_student:
                if assignment_name in student.assignments:
                    del student.assignments[assignment_name]
                    return()

    def delete_assignment_classroom(self, assignment_name):
        for student in self.roster.values():
            if assignment_name in student.assignments:
                del student.assignments[assignment_name]

    def edit_student_assignment(self, current_student, assignment_name, grade):
        for student in self.roster.values():
            if student.name == current_student:
                for assignment in student.assignments:
                    if assignment == assignment_name:
                        student.assignments[assignment] = grade
                        print("assignment modified")
                        return()

    def update_gpa_classroom(self):
        class_total = 0
        student_count = len(self.roster)
        for student in self.roster.values():
            student.update_grade_in_class()
            class_total += student.grade_in_class
            if student.grade_in_class == 0:
                student_count -= 1
        self.classroom_gpa = class_total / student_count


classroom_1 = Classroom("Math", "Fred")
print(classroom_1.classroom_name)

classroom_1.create_student("John")

classroom_1.add_assignment_student("John", "Pizza", 5)
john = classroom_1.roster[1]
print(john.assignments)

classroom_1.create_student("Tony")
print(classroom_1.roster.values)

classroom_1.add_assignment_student("Tony", "Pasta", 7)
tony = classroom_1.roster[2]
print(tony.assignments)

classroom_1.edit_student_assignment("John", "Pizza", 35)
john = classroom_1.roster[1]
print(john.assignments)

classroom_1.delete_assignment_student("John", "Pizza")
john = classroom_1.roster[1]
print(john.assignments)

classroom_1.add_assignment_classroom("Beer", 100)
tony = classroom_1.roster[2]
print(tony.assignments)

classroom_1.delete_assignment_classroom("Beer")
tony = classroom_1.roster[2]
print(tony.assignments)

classroom_1.update_gpa_classroom()
print("====")
print(classroom_1.classroom_gpa)
