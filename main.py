class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.posts = []
        self.following = []
        self.followers = []

    def create_post(self, content):
        post = Post(content)
        self.posts.append(post)

    def follow(self, user):
        self.following.append(user)
        user.followers.append(self)

    def unfollow(self, user):
        self.following.remove(user)
        user.followers.remove(self)

class Post:
    def __init__(self, content):
        self.content = content
        self.likes = []

    def like(self, user):
        self.likes.append(user)

class Like:
    def __init__(self, user, post):
        self.user = user
        self.post = post

class SocialNetwork:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def get_post(self, user, post_index):
        return user.posts[post_index]

    def like_post(self, user, post_index, liker):
        post = self.get_post(user, post_index)
        post.like(liker)

    def follow(self, user1, user2):
        user1.follow(user2)

    def unfollow(self, user1, user2):
        user1.unfollow(user2)

social_network = SocialNetwork()
user1 = User("user1", "user1@example.com")
user2 = User("user2", "user2@example.com")
user3 = User("user3", "user3@example.com")

social_network.add_user(user1)
social_network.add_user(user2)
social_network.add_user(user3)

user1.create_post("Hello, world!")
user2.create_post("Hi, everyone!")

social_network.follow(user1, user2)
social_network.follow(user1, user3)

social_network.like_post(user1, 0, user2)

print(len(user1.following))
print(len(user2.followers))
print(len(user1.posts[0].likes))