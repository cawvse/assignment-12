"""
A Student class.

@author GCCIS Faculty
"""

__GRADES = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F", "NG"]

__GRADE_WEIGHT = {
    __GRADES[0]: 4.0,
    __GRADES[1]: 3.67,
    __GRADES[2]: 3.33,
    __GRADES[3]: 3.0,
    __GRADES[4]: 2.67,
    __GRADES[5]: 2.33,
    __GRADES[6]: 2.0,
    __GRADES[7]: 1.67,
    __GRADES[8]: 1.0,
    __GRADES[9]: 0,
    __GRADES[10]: 0 # no grade
}

class Student:
    """
    A class that represents a student with fields for ID, name, credits, and
    GPA.
    """
    __slots__ = ["id", "name", "credits", "gpa"]

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.credits = 0
        self.gpa = 0

def print_student(student):
    """
    Prints a student's info to standard output.
    """
    print("Student: ID=", student.id, ", name=", student.name, 
        ", credits=", student.credits, ", GPA=", student.gpa, sep="")