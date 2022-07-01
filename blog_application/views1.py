from blog_application.model import users,posts

session = {}

def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            return None
    return wrapper


def authenticate(**kwargs):
    uname = kwargs.get("username")
    pwd = kwargs.get("password")
    user = [user for user in users if user["username"] == uname and user["password"] == pwd]
    return user


# print(authenticate(username="akhil",password="Password@123"))



class LoginView:
    def post(self, **kwargs):
        uname = kwargs.get("username")
        pwd = kwargs.get("password")
        user = authenticate(username=uname, password=pwd)
        if user:
            session["user"] = user[0]


login = LoginView()
login.post(username="akhil", password="Password@123")
print(session)

class PostListView:
    @signin_required
    def get(self,*args,**kwargs):
        return posts
    @signin_required
    def get_user_wise(self,*args,**kwargs):
        pst=[post for post in posts if post["userId"]==kwargs.get("userId")]
        return pst

    @signin_required
    def post(self,*args,**kwargs):
        post=kwargs.get("data")
        post["userId"]=session["user"]["id"]
        posts.append(post)
        print(posts[-1])

class Liked_By:

    @signin_required
    def like(self,*args,**kwargs):
        postid=kwargs.get("postId")
        post=[post for post in posts if post["postId"]==postid]

        if post:
            post=post[0]
            post.get("liked_by").append(session["user"]["id"])
            print(post["liked_by"])


my_post = {"postId":9,"title":"mytitle","content":"mycontent","liked_by":[]}

allpost=PostListView()
allpost.post(data=my_post)
print(allpost.get())

print(allpost.get_user_wise(userId=2))

like=Liked_By()
like.like(postId=1)

st=set()






