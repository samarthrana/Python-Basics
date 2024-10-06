#email = campusx@gmail.com
#password = 1234

email = input("Enter email: ")
if "@" in email:
    password = input("Enter password: ")

    if email == "campusx@gmail.com" and password == "1234":
        print("Welcome")
    elif email == "campusx@gmail.com" and password != "1234":
        print("Re-Enter password")
        password = input("Enter password: ")
        if password != "1234":
            print("Still incorrect")
    else:
        print("Wrong credentials")
else:
    print("Enter correct email format.")