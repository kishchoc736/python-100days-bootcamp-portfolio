# there is no block scope in python
game_level = 10
enemies = ["skeleton", "zombie", "alien"]

def create_enemy():
    # Initialisation of the variable to
    # allow the function to run even if no assignment occurs
    new_enemy = ""
    if game_level > 5:
        new_enemy = enemies[0]

# See how this is not accessible when not within a function
# print(new_enemy)

# if you indent it, then it can be accessed
    print(new_enemy)

create_enemy()

