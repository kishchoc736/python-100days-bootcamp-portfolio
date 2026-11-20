# use pass to just skip to next line
# PascalCase
# camelCase
# snake_case


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        # Initialized for us
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1





user_1 = User("001", "Kishore")
user_2 = User("002", "Akshay")

user_1.follow(user_2)

print(f"User 1's follower count: {user_1.followers}")
print(f"User 1's following count: {user_1.following}")

print("\n")


print(f"User 2's follower count: {user_2.followers}")
print(f"User 2's following count: {user_2.following}")
