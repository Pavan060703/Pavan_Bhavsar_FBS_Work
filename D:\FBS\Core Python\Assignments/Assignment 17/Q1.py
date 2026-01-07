class Student:
    def __init__(self,student_id,name,age,percentage):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.percentage=percentage

    def accept(self):
        self.student_id=int(input("Enter student id:"))
        self.name=input("Enter the name:")
        self.age=int(input("Enter the age:"))
        self.percentage=float(input("Enter the percentage:"))
    
    def display(self):
        print("Student id is : ",self.student_id)
        print("Student name is : ",self.name)
        print("Student age is : ",self.age)
        print("Student percentage is : ",self.percentage)

    def calculateRank(self):
        if self.percentage>=85:
            print("Rank is A")
        elif self.percentage<85 and self.percentage>=70:
            print("Rank is B")
        elif self.percentage<70 and self.percentage>=55:
            print("Rank is C")
        elif self.percentage<55 and self.percentage>=35:
            print("Rank is D")
        else:
            print("Fail")

    def __str__(self):
        return f"Student id is {self.student_id} \nStudent Name is {self.name} \nstudent age is{self.age} \n Student percentage is {self.percentage}"
    

s1=Student(101,"Pavan Bhavsar",22,85)
s1.display()
s1.calculateRank()