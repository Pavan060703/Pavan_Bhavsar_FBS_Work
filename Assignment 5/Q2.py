#Enter number of students from user. For those many students accept marks of 5 subject marks from user 
#and calculate percentage . Display all percentage and average percentage of students. 
number_of_students=int(input("Enter number of students"))
total_percentage_sum=0
for i in range(number_of_students):
    print(f"\n Enter the marks of student {i+1}: ")
    total=0

    for j in range(5):
        marks=float(input(f"Enter marks of subject {j+1}:"))
        total+=marks

    percentage=(total/500)*100
    total_percentage_sum+=percentage

    print(f"Percentage of student {i+1}:{percentage:.2f}%")

average_percentage = total_percentage_sum/number_of_students
print(f"\n Average percentage of all students : {average_percentage:.2f}%")