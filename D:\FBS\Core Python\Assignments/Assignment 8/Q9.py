def isPalindrome(num):
    temp=num
    reverse=0
    while temp>0:
        digit=temp%10
        reverse=reverse*10+digit
        temp=temp//10
    
    if reverse==num:
        print("This number is palindrome")
    else:
        print("This number is not palindrome")

num=int(input("Enter the number"))
isPalindrome(num)
