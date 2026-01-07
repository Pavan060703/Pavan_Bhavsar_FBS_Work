person1=int(input("Enter the age of first person"))
person2=int(input("Enter the age of second person"))
person3=int(input("Enter the age of third person"))
person4=int(input("Enter the age of fourth person"))
person5=int(input("Enter the age of fifth person"))
ticket=int(input("Enter the per person ticket amount"))

total_amount=0
if(person1<12):
    amount=ticket-(ticket*30/100)
elif(person1>59):
    amount=ticket-(ticket*50/100)
else:
    amount1=ticket

if(person2<12):
    amount2=ticket-(ticket*30/100)
elif(person2>59):
    amount2=ticket-(ticket*50/100)
else:
    amount2=ticket

if(person3<12):
    amount3=ticket-(ticket*30/100)
elif(person3>59):
    amount3=ticket-(ticket*50/100)
else:
    amount3=ticket

if(person4<12):
    amount4=ticket-(ticket*30/100)
elif(person4>59):
    amount4=ticket-(ticket*50/100)
else:
    amount4=ticket

if(person5<12):
    amount5=ticket-(ticket*30/100)
elif(person5>59):
    amount5=ticket-(ticket*50/100)
else:
    amount5=ticket

total_amount=amount1+amount2+amount3+amount4+amount5
print(total_amount)