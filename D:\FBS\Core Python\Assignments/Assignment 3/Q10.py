person_age=int(input("Enter the age of person "))
gender=input("Enter the gender of person (male/female) ")
if(gender=="male"):
    if(person_age>=21):
        print("Eligible to marry")
    else:
        print("Not Eligible")
else:
    if(person_age>=18):
        print("Eligible to marry")
    else:
        print("Not Eligible")