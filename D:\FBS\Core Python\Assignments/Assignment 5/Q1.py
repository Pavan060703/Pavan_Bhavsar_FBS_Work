# Write a program to prompt user to enter userid and password If ID and password is incorrect give him chance to reenter the credentials. Let him try 
# 3 times. After that program to terminate.
correct_id="admin"
correct_password="admin@123"
for i in range(3):
    user_id=input("Enter User ID")
    password=input("Enter Password:")

    if user_id==correct_id and password==correct_password:
        print("Login Successful")
        break
    else:
        print("Incorrect useid or password . Try again")
        print("Attempts left", 2 - i)

else:
    print("You have exceeded maximum attempts")