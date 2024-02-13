import os
username= "python"
password= "1234"


givenUsername=input("Enter Your username: ")

if givenUsername == username:
    print("Correct Username")
    givenPassword= input("Enter your password: ")
    if givenPassword ==password:
        print("Correct Password")
        os.system("figlet LOG IN SUCCESS")
    else:
        print("Wrong Password")


else:
    print(
        "Wrong User"
    )
