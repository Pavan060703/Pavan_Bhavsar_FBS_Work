def power_series(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+(i*i)
        
    return sum

print(power_series(5))