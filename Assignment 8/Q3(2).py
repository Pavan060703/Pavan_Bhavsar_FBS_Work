def fact_series(n):
    if n<=0:
        return 0
    fact=1
    sum=0
    for i in range(1,n+1):
        fact=fact*i # factorial      
        sum=sum+fact # Addition of factorial

    return sum

print(fact_series(1))

