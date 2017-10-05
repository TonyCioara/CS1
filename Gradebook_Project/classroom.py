from student import Student


class Classroom(Object):
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

        get_assignment_name_clasroom(self):
            is_complete = 0
            While is_complete is False
                get inport for assignment_name
                is_complete = 1
                Run through array of students_array
                    check if assignment_name exists
                        if True is_complete = 0

        get_assignment_name_student(self, student):
            is_complete = 0
            While is_complete is False
                get inport for assignment_name
                is_complete = 1
                check if assignment_name exists
                    if True is_complete = 0

        display_student(self):
            Ask for student name
            Print all assignments, grades, and GPA

        display_classroom(self):
            Print every student in a new line, alongside assignments, grades,
            and GPA

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
                Remove assigment


    '''
