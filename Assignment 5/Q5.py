# # Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount. (Use looping to optimize
# the problem)
amount=int(input("Enter the amount:"))
notes=[2000,500,200,100,50,20,10,5,2,1]
i=0
total_notes=0

while amount>0 and i<len(notes):
    note=notes[i]
    if amount>=note:
        count=amount//note
        print(f"{note} Rs note:{count}")
        total_notes+=count
        amount=amount%note
    i+=1

print("Minimum number of notes needed :", total_notes)