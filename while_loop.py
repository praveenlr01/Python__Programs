username=" "
password=" "
while True:
    opt=int(input("Click [1] to create \nClick [2] to Login \nEnter: "))
    if opt==1:
        user=input("Enter your user name: ")
        passwrd=input("Enter your password: ")
        username=user
        password=passwrd
        print("Created Successfully..")
    elif opt==2:
        u=input("Enter your username: ")
        if u==username:
            p=input("Enter your password: ")
            if p==password:
                print("Login Successfully..")
                like=0
                commant=0
                post=0
                while True:
                    profile=int(input("click [1] to give like \nClick [2] to commant \nClick [3] to view post \nClick[4] to LogOut \nEnter: "))
                    if profile==1:
                        like +=1
                        print("Like = ",like)
                    elif profile==2:
                        commant+1
                        print("commant = ",commant)
                    elif profile==3:
                        post+=1
                        print("post = ",post)
                    elif profile==4:
                        print("Logout Successfully")
                        break
                    else:
                        print("Invalid choice:  ")
            else:
                print("invalid password")
        else:
            print("invalid username")
    else:
        print("Invalid choice")
