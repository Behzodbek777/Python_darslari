class Student():
    sanagich = 0

    def __init__(self):
        Student.sanagich += 1


s1 = Student()
s2 = Student()
s3 = Student()
print(Student.sanagich)
