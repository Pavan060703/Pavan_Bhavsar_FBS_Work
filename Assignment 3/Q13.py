electricity_unit=float(input("Enter the electricity units"))
electricity_bill=0
if(electricity_unit<=50):
    electricity_bill=electricity_unit*0.50
elif(electricity_unit>50 or electricity_unit<=150):
    electricity_bill=electricity_unit*0.75
elif(electricity_unit>100 or electricity_unit<=250):
    electricity_bill=electricity_unit*1.20
elif(electricity_unit>250):
    electricity_bill=electricity_unit*1.5
    
else:
    print()
    
    

print(electricity_bill)