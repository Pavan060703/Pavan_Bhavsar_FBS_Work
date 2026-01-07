a=float(input("Enter the coefficient of a"))
b=float(input("Enter the coefficient of b"))
c=float(input("Enter the coefficient of c"))

root_1= (-b+((b**2)-(4*a*c))**0.5)/2*a

root_2= (-b-((b**2)-(4*a*c))**0.5)/2*a

print("First root is :",root_1)
print("Second root is :",root_2)
