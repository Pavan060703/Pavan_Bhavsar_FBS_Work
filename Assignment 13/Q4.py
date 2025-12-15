# Python program to Generate a Dictionary that contains numbers (between 1 and N) in the form
#(x,x*x)
def Generate_Dictionary(n):
    new_dict={}
    for x in range(1,n+1):
        new_dict[x]=x*x

    return new_dict

n=int(input("Enter a number"))
new_dict=Generate_Dictionary(n)
print(new_dict)