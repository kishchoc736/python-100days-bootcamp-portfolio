import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]



# way 1
random_index = random.randint(0, 4)
print(friends[random_index])

# way 2: or use the random.choice() method

print(random.choice(friends))

