from blog_application.model import users
from blog_application.model import posts

class User:
    id:int
    user_name:str
    email:str
    password:str

    def add_user(self,**kwargs):
        self.id=kwargs.get("id")
        self.user_name=kwargs.get("user_name")
        self.email=kwargs.get("email")
        self.password=kwargs.get("password")

        users.append({"id":self.id,"username":self.user_name,"email":self.email,"password":self.password})

    def login(self,**kwargs):
        flag=["Logged In" if user["email"]==kwargs.get("email") and user["password"]==kwargs.get("password") else "Access Denied" for user in users]
        print(flag[0])

    def __str__(self):
        return str(self.id)

blog_user=User()
blog_user.login(email="akhil@gmail.com",password="Password@123")
blog_user.add_user(id=7,user_name="vishnu",email="vishnucr3000@gmail.com",password="Password@123")


class Posts(User):
    postId:int
    userId:int
    title:str
    content:str
    liked_by:list

    def add_post(self,**kwargs):
        self.id=kwargs.get("id")
        self.userId=blog_user.id
        self.title=kwargs.get("title")
        self.content=kwargs.get("content")
        self.liked_by=[]

        posts.append({"postId":self.id,"UserId":self.userId,"title":self.title,"content":self.content,"liked_by":[]})

    def likepost(self,liked)->bool:

        self.like=liked

        if self.like==True:
            posts["liked_by"]

new_post=Posts()
new_post.add_post(id=9,title="vishnus",content="test")
print(posts)



