class Student:
    Students = []
    empty_tuple = ()
    def __init__(self,student_id, student_name, email, grades=None, courses=None):
        self.id_name = (student_id, student_name)
        self.email = email
        self.grades = {}
        for score, subject in grades:
            grades[subject] = 
        self.courses = courses

    def __str__(self):
       
