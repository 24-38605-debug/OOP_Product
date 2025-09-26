#I named the class 'Student' as instructed, then I input the required information for students such as the id 
# (with unique identification using number), name, email, grades and course. I set the grades as empty dictionary and the courses as empty set.
class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.id_name = (student_id, student_name)
        self.email = email
        self.grades = grades if grades else {}
        self.courses = courses if courses else set()

#I set the method with return to call back the value of a function

    def __str__(self):
        return (
            f"ID: {self.id_name[0]}, Name: {self.id_name[1]}, "
            f"Email: {self.email}, Grades: {self.grades}, "
            f"Courses: {', '.join(self.courses)}"
        )


#then I set the students as an empty list, which I will store all the information of students
class StudentRecords:
    def __init__(self):
        self.students = []

#this method will add and create a new student using the information of id, name, email, grades, and course.

    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        new_student = Student(student_id, student_name, email, grades, courses)
        self.students.append(new_student)
        return "Student added successfully"
    
#this updates the following information of the students, and this allows you to find the student using their unique IDs.

    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:
            if student.id_name[0] == student_id:
                if email is not None:
                    student.email = email
                if grades is not None:
                    student.grades.update(grades)
                if courses is not None:
                    student.courses.update(courses)
                return "Student updated successfully"
        return "Student not found"

#this method will allow you to delete the specific student using the the ID, therefore it will print 
#'student not found' if you enter an ID that is not in the class.
    def delete_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                self.students.remove(student)
                return "Student deleted successfully"
        return "Student not found"
    
#allows you to add new courses to a specific student 
    def enroll_course(self, student_id, course):
        for student in self.students:
            if student.id_name[0] == student_id:
                student.courses.add(course)
                return "Course added successfully"
        return "Student not found"

#you can look through the program on a specific student by using the ID 
    def search_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                return str(student)
        return "Student not found"

records = StudentRecords()
print(records.add_student(1, "Ernalyn Montefalco", "eerna123@email.com", {"Math": 82}, {"Math"}))
records.add_student(2, "Juan Dela Cruz Magpantay", "jmagpantay@email.com")
print(records.update_student(1, grades={"Science": 95}))
print(records.enroll_course(2, "Filipino"))
print(records.search_student(3))
print(records.delete_student(2))

