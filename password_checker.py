print("Press\n 1. Login \n 2. Signup \n 3. Change Password")

n=int(input())
if n==1:
    print("Enter your password")
    pwd=input()
    file=open("password.txt",'r')
    k=file.read()
    file.close()
    if pwd==k:
        print("Correct Password")
    else:
        print("Wrong Password")
elif n==2:
    file=open("password.txt",'w')
    print("Enter your new password")
    pwd=input()
    print("Confirm ur password")
    pwd1=input()
    if  pwd == pwd1:
        file.write(pwd)
        file.close()
    else:
        print("Password does not match ")
elif n==3:
    print("Enter your old password")
    pwd=input()
    file=open("password.txt",'r')
    k=file.read()
    file.close()

    if pwd==k:
        print("New Password")
        pwd=input()
        file=open("password.txt",'w')
        file.write(pwd)
        file.close()
    else:
        print("You have entered wrong Password")
exit()

    
