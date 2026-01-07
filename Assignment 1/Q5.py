#Compound Interest
p=float(input("Enter the principal"))
t=float(input("Enter the years"))
r=float(input("Enter the rate of interest"))
A=p*(1+r/100)**t

C_I=A-p
print("Compound Interest is ",C_I)
