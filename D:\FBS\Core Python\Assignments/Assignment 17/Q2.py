from Q1 import Student
class EnggStudent(Student):
    def __init__(self,student_id,name,age,percentage,branch,internalMarks):
        super().__init__(student_id,name,age,percentage)
        self.branch=branch
        self.internalMarks=internalMarks
    
    def accept(self):
        super().accept()
        self.branch=input("Enter the branch : ")
        self.internalMarks=int(input("Enter the internalMarks"))

    def display(self):
        super().display()
        print("Branch : ",self.branch)
        print("Internal Marks : ",self.internalMarks)

    def calculateRank(self):
        total_score=(self.percentage+self.internalMarks)/2
        if total_score>=85:
            print("First class with distinction")
        elif total_score<85 and total_score>=70:
            print("First Class")
        elif total_score<70 and total_score>=60:
            print("Second Class")
        elif total_score<60 and total_score>=45:
            print("Third class")
        elif total_score<45 and total_score>-35:
            print("Pass")
        else:
            print("Fail")
    
    def __str__(self):
        return f"Student Id is {self.student_id} \n Student Name is {self.name} \n Student age is {self.age} \n Student Percentage is {self.percentage} \n Student Branch is {self.branch} \n Student internal marks is {self.internalMarks}"

s1=EnggStudent(101,"Pavan Bhavsar",22,90,"CSE-AI",85)
s1.accept()
s1.calculateRank()    
    