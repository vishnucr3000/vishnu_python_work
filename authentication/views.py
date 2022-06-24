from authentication.models import users

class Authentication:
    user_name:str
    password:str


    def login(self,**kwargs):
        uname=kwargs["user_name"]
        pwd=kwargs["password"]

        flag=["Loggin sucessful" if user["username"]==uname and user["password"]==pwd else "Wrong Credentials" for user in users]
        print(flag[0])


    def logout(self,args):
        if args=="logout":
            print("logged out")

    def change_password(self,*args):
        uid=args[0]
        newpwd=args[1]

        for user in users:
            if user["id"]==uid:
                user["password"]=newpwd
                print("Password Changed")
            break










auth=Authentication()
auth.login(user_name="django",password="django@123")
auth.logout("logout")
auth.change_password(1,"vishnu")
print(users)