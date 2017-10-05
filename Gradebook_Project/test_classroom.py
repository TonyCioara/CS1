from student import Student
import pytest


def set_up_test():
    student = Student("Student McStudentFace", 1)
    return student


def test_setup():
    student = setup_for_test()
    assert student.name == "Student McStudentFace"
    assert student.student_ID == 1
    assert student.grade_in_class == None
    assert len(student.assignments) == 0
