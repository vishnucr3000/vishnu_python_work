import json

with open("blog.json", encoding="utf-8") as f:
    data = json.load(f)
    print(len(data))

# number of post by user id=1

posts = len([post for post in data if post["userId"] == 1])
print(posts)


# total number of likes of post id 6

num_like=[len(post["liked_by"]) for post in data if post["postId"]==6]
print(num_like)

# total number of likes by userid=2

num_like_post=[post for post in data if 2 in post["liked_by"]]

print(len(num_like_post))


