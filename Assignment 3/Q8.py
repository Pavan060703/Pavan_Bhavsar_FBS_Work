userid=input("Enter the userid ")
password=input("Enter the password ")

if(userid=="1234" and password=="Pavan@123"):
    print("Captcha=3f67He")
    Captcha=input("Enter the captcha")
    if(Captcha=="3f67He"):
        print("Success")
    else:
        print("Failed")
else:
    print("Wrong Credentials")

          