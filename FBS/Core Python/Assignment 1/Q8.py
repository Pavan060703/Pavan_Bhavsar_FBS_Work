days=int(input("Enter the days that you want to convert in years , month, day"))

year=days//365

remaining=days%365

weeks=remaining//7

Days=remaining%7

print("Years:",year)
print("Weeks:",weeks)
print("days:",Days)
