# Create a class College which has collection of students. 
class Student:
    def __init__(self,sid,sname):
        self.id=sid
        self.sname=sname

    def __str__(self):
        return f"Student Id : {self.id},Name : {self.sname}"
    
class College:
    def __init__(self,no_of_students):
        self.no_of_students=no_of_students
        self.students=[]

    def addStudent(self,student):
        if len(self.students)<self.no_of_students:
            self.students.append(student)
            print("Student added successfully")
        else:
            print("College is full")

    def getStudent(self,sid):
        for student in self.students:
            if student.id==sid:
                self.students.remove(student)
                print("Student removed successfully")
                return 
        print("Student not found")
    def __str__(self):
        if not self.students:
            return "No students in college"
        return "\n".join(str(student) for student in self.students) 
    
c1=College(1)
s1=Student(101,"Pavan Bhavsar")
c1.addStudent(s1)



