from Q1 import Student

class MedicalStudent(Student):
    def __init__(self,student_id,name,age,percentage,specialization,marksOfIntership):
        super().__init__(self,specialization,marksOfIntership)
        self.specialization=specialization
        self.marksOfInternship=marksOfIntership
    
    def accept(self):
        super().accept()
        self.specialization=input("Enter the specialization:")
        self.marksOfInternship=int(input("Enter the marks of internship:"))

    def display(self):
        super.display()
        print("Specialization is ",self.specialization)
        print("Marks of Internship is ",self.marksOfInternship)

    def calculateRank(self):
        super().calculateRank()
        final_score=(self.percentage+self.marksOfInternship)/2
        if final_score>=85:
            print("First class with distinction")
        elif final_score<85 and final_score>=60:
            print("First Class")
        elif final_score<60 and final_score>=50:
            print("Second Class")
        elif final_score<50 and final_score>=45:
            print("Third Class")
        elif final_score<45 and final_score<=35:
            print("Fourth Class")
        else:
            print("Fail")
    
    def __str__(self):
        return f"Student Id : {self.student_id} \n Student Name is : {self.name} \n Student age is : {self.age} \n Student percentage is : {self.percentage} \n Student specialization is : {self.specialization} \n Student's marks of intership : {self.marksOfInternship}"

s1=MedicalStudent(101,"Pavan Bhavsar",22,85,"Artificial Intelligence",80)
s1.display()
s1.calculateRank()

