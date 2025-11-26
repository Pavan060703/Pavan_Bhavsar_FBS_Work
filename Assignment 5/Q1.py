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